from SolveSuperMarioPets.OtherFunctions import *

class Party():
    def copy(self):
        newPartyPets = []
        for pet in self.partyPets:
            newPet = pet.copy()
            newPartyPets.append(newPet)
        return newPartyPets

    def __init__(self, myPets, battle=None):
        self.battle = battle
        self.partyPets = []
        for pet in myPets:
            self.partyPets.append(pet)

    def is_alive(self):
        if self.len() > 0:
            return True
        return False

    def len(self):
        return len(self.partyPets)
    def position(self, pet):
        return self.partyPets.index(pet)
    def low_health_pet(self):
        low_health_pet = self.partyPets[0]
        for pet in self.partyPets:
            if pet.health < low_health_pet.health:
                low_health_pet = pet
        return low_health_pet
    def high_health_pet(self):
        high_health_pet = self.partyPets[0]
        for pet in self.partyPets:
            if pet.health > high_health_pet.health:
                high_health_pet = pet
        return high_health_pet

    def printF(self):
        for pet in self.partyPets:
            pet.print()
    def printB(self):
        for pet in reversed(self.partyPets):
            pet.print()

    def start_battle(self, other_party):
        shots_fired = False
        for pet in self.partyPets:
            shots_fired = pet.start_battle(self, other_party) or shots_fired
        return shots_fired

    def faint_scan(self, other_party):
        shots_fired = False
        fainted_pets = []
        old_party = self.copy()
        for pet in self.partyPets:
            if pet.health <= 0:
                fainted_pets.append([pet, self.position(pet)-len(fainted_pets)])
        for pet in fainted_pets:
            self.partyPets.remove(pet[0])
        for pet in fainted_pets:
            shots_fired = pet[0].faint(pet[1], self, other_party) or shots_fired
        for pet in self.partyPets:
            pet.friend_has_fainted(len(fainted_pets), old_party, self)
        return shots_fired

    def spawn(self, pets, location=0):
        for new_pet in pets:
            if self.len() < 5:
                for pet in self.partyPets:
                    pet.new_pet_spawning(new_pet)
                self.partyPets.insert(location, new_pet)

    def take_damage(self, damage_array, other_party):
        for i in range(0, len(self.partyPets)):
            self.partyPets[i].take_damage(damage_array[i], self, other_party)

    def before_attack(self, other_party):
        return self.partyPets[0].before_attack(self, other_party)

    def make_attack(self, other_party):
        self.partyPets[0].make_attack(self, other_party)

    def after_attack(self, other_party):
        shots_fired = False
        for i in range(0, self.len()):
            shots_fired = self.partyPets[i].after_attack(i, self, other_party) or False
        return shots_fired
