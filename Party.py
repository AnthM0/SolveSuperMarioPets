from OtherFunctions import *

class Party():
    def copy(self):
        newPartyPets = []
        for pet in self.partyPets:
            newPet = pet.copy()
            newPartyPets.append(newPet)
        return newPartyPets

    def __init__(self,myPets,battle=None):
        self.battle = battle
        self.partyPets = []
        for pet in myPets:
            self.partyPets.append(pet)
            pet.addToParty(self)

    def isAlive(self):
        if(len(self.partyPets) > 0):
            return True
        return False

    def len(self):
        return len(self.partyPets)

    def printF(self):
        for pet in self.partyPets:
            pet.print()
    def printB(self):
        for pet in reversed(self.partyPets):
            pet.print()

    def faintScan(self):
        for pet in self.partyPets:
            if(pet.health <= 0):
                newPetList = pet.faint()
                for newPet in newPetList:
                    self.spawn(newPet)
                self.partyPets.remove(pet)

    def spawn(self, pet):
        if(self.len() < 5):
            self.partyPets.insert(0,pet)

    def startBattle(self,lenOtherParty):
        damage = arrZeros(lenOtherParty)
        for pet in self.partyPets:
            damage = addArr(damage, pet.startBattle(lenOtherParty))
        return damage

    def takeDamage(self,damageArr):
        for i in range(0,len(self.partyPets)):
            self.partyPets[i].takeDamage(damageArr[i])
        self.faintScan()

    def getTurnDamage(self,lenOtherParty):
        damage = arrZeros(lenOtherParty)
        for i in range(0, len(self.partyPets)):
            damage = addArr(damage, self.partyPets[i].getAttack(lenOtherParty,i))
        return damage