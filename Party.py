from SolveSuperMarioPets.Pets import *


class Party:
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
    def hash_string(self):
        ret_str = ""
        for pet in self.partyPets:
            ret_str = ret_str + "(" + pet.hash_string() + ")"
        return ret_str

    def is_alive(self):
        if self.len() > 0:
            return True
        return False

    def len(self):
        return len(self.partyPets)
    def position(self, pet):
        if pet not in self.partyPets:
            return -1
        return self.partyPets.index(pet)
    def tiger_lv(self, location):
        if self.len() > location:
            return self.partyPets[location].tiger_lv()
        return 0
    def low_health_pet(self):
        low_health_pet = self.partyPets[0]
        for pet in self.partyPets:
            if pet.health < low_health_pet.health:
                low_health_pet = pet
        return low_health_pet
    def high_health_pet(self):
        high_health_pet = self.partyPets[0]
        for pet in self.partyPets:
            if pet.health >= high_health_pet.health:
                high_health_pet = pet
        return high_health_pet
    def pet_names(self):
        names = []
        for pet in self.partyPets:
            names.append(pet.name)
        return names

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
        old_party = Party(self.copy())
        for pet in self.partyPets:
            if pet.health <= 0:
                fainted_pets.append([pet, self.position(pet)-len(fainted_pets)])
            else:
                shots_fired = pet.was_hurt(self, other_party) or shots_fired
        for pet in fainted_pets:
            self.partyPets.remove(pet[0])
        for pet in fainted_pets:
            shots_fired = pet[0].faint(pet[1], self, other_party) or shots_fired
        for pet in fainted_pets:
            if other_party.len() > 0:
                shots_fired = other_party.partyPets[0].foe_has_fainted(pet[1], other_party, self) or shots_fired
        FlySkip = 0
        for pet in self.partyPets:
            if FlySkip == 0:
                FlySkip = pet.friend_has_fainted(len(fainted_pets), old_party, self)
            else:
                FlySkip -= 1
        return shots_fired

    def spawn(self, pets, location=0):
        success = False
        for new_pet in pets:
            if self.len() < 5:
                for pet in self.partyPets:
                    pet.new_pet_spawning(new_pet, self)
                self.partyPets.insert(location, new_pet)
                success = True
        return success

    def before_attack(self, other_party):
        return self.partyPets[0].before_attack(self, other_party)

    def make_attack(self, other_party):
        self.partyPets[0].make_attack(self, other_party)
        if self.len() > 1:
            self.partyPets[1].friend_in_front_attacked = True

    def after_attack(self, other_party):
        shots_fired = False
        for i in range(0, self.len()):
            shots_fired = self.partyPets[i].after_attack(self, other_party) or shots_fired
        return shots_fired
