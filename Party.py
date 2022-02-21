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
    def lowHealthIndex(self):
        lowHealth = 100
        retIndex = 0
        for i in range(0,self.len()):
            if(self.partyPets[i].health < lowHealth):
                lowHealth = self.partyPets[i].health
                retIndex = i
        return retIndex

    def printF(self):
        for pet in self.partyPets:
            pet.print()
    def printB(self):
        for pet in reversed(self.partyPets):
            pet.print()

    # def faintDamageScan(self):
    #     faintDamageFlag = False
    #     myPartyDamageArr = arrZeros(self.len(),0)
    #     otherPartyDamageArr = arrZeros(5,0)
    #     for pet in self.partyPets:
    #         if(pet.health <= 0):
    #             faintDamageArr = pet.faintDamage(1, self.len(), 5)
    #             if(faintDamageArr[0]):
    #                 faintDamageFlag = True
    #                 myPartyDamageArr = addArr(myPartyDamageArr,faintDamageArr[1])
    #                 otherPartyDamageArr = addArr(otherPartyDamageArr, faintDamageArr[2])
    #     return([faintDamageFlag,myPartyDamageArr,otherPartyDamageArr])

    def faintScan(self):
        faintedPets = [["PH"]]
        for pet in self.partyPets:
            if(pet.health <= 0):
                indexOfPet = self.partyPets.index(pet)
                faintedPets.append([pet, indexOfPet])
                self.partyPets.remove(pet)
        faintedPets.remove(["PH"])
        ##print(faintedPets)
        for petArr in faintedPets:
            petBoosts = petArr[0].faintBoost(self.len())
            for i in range(0, self.len()):
                self.partyPets[i].boostFromFaint(petBoosts[i])
        for petArr in faintedPets:
            newPetList = petArr[0].faintSpawn()
            for newPet in newPetList:
                self.spawn(newPet, petArr[1])

    def spawn(self, newPet, location=0):
        if(self.len() < 5):
            addition = [0, 0]
            for pet in self.partyPets:
                addition = addArr(addition, pet.petSpawned())
            newPet.boost(addition)
            self.partyPets.insert(location,newPet)

    def startBattleDamage(self,lenOtherParty,lowHealthIndex):
        damage = arrZeros(lenOtherParty)
        for pet in self.partyPets:
            damage = addArr(damage, pet.startBattleDamage(lenOtherParty,lowHealthIndex))
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