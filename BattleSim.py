import random
from Pets import *

def arrZeros(length):
    arr = []
    for i in range(0,length):
        arr.append(0)
    return arr

def addArr(arr1, arr2):
    newArr = []
    for i in range(0,len(arr1)):
        newArr.append(arr1[i] + arr2[i])
    return newArr

class Party():
    def copy(self):
        self.partyPets = []
        return self
    def __init__(self,myPets, battle=None):
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
                pet.faint()
                self.partyPets.remove(pet)
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


class Battle:
    def __init__(self,myPets,otherPets):
        self.myParty = Party(self, myPets)
        self.otherParty = Party(self, otherPets)
    def printBattle(self):
        lenMyParty = len(self.myParty.partyPets)
        for i in range(lenMyParty,5):
            print(" ", end="")
        self.myParty.printB()
        print("    ", end="")
        self.otherParty.printF()
        print()
    def startBattle(self):
        myDamage = self.myParty.startBattle(self.otherParty.len())
        otherDamage = self.otherParty.startBattle(self.myParty.len())
        print("Start Battle:", otherDamage, "   ", myDamage)
        self.myParty.takeDamage(otherDamage)
        self.otherParty.takeDamage(myDamage)
    def singleAttack(self):
        myDamage = self.myParty.getTurnDamage(self.otherParty.len())
        otherDamage = self.otherParty.getTurnDamage(self.myParty.len())
        print("Attack: ", otherDamage, "   ", myDamage)
        self.myParty.takeDamage(otherDamage)
        self.otherParty.takeDamage(myDamage)
    def checkOutcome(self):
        if(self.myParty.isAlive() and self.otherParty.isAlive()):
            return 69
        elif(self.myParty.isAlive()):
            return 1
        elif(self.otherParty.isAlive()):
            return -1
        return 0

class Simulator:
    def __init__(self,myPets,otherPets):
        self.myParty = myPets
        self.otherParty = otherPets
    def __init__(self):
        self.myParty = [Fish(), Fish(), Fish()]
        self.otherParty = [Mosquito(), Mosquito(), Mosquito(), Mosquito()]
    def runSingleBattle(self,myPets,otherPets,printing):
        thisBattle = Battle(myPets, otherPets)
        if(printing):
            thisBattle.printBattle()
        thisBattle.startBattle()
        if(printing):
            thisBattle.printBattle()
        outcome = 69
        while outcome == 69:
            thisBattle.singleAttack()
            if(printing):
                thisBattle.printBattle()
            outcome = thisBattle.checkOutcome()
        return outcome
    def runMultiBattle(self,tests):
        wins = 0
        ties = 0
        losses = 0
        for i in range(0,tests):
            myPetsParty = [Fish(), Fish(), Fish()]
            otherPetsParty = [Mosquito(), Mosquito(), Mosquito(), Mosquito()]
            outcome = self.runSingleBattle(myPetsParty,otherPetsParty,False)
            if(outcome == 1):
                wins += 1
            elif(outcome == -1):
                losses += 1
            else:
                ties += 1
        winP = wins*100 / tests
        tieP = ties*100 / tests
        lossP = losses*100 / tests
        print("Win(", winP, "%), Tie(", tieP, "%), Loss(", lossP, "%)")

myPetsParty = [Fish(), Fish(), Fish()]
otherPetsParty = [Mosquito(), Mosquito(), Mosquito(), Mosquito()]
# fakeBattle = Battle(myPetsParty, otherPetsParty)
# fakeBattle.printBattle()
#
# battleSim = Simulator()
# battleSim.runSingleBattle(myPetsParty,otherPetsParty,True)

myFirstParty = Party(myPetsParty)
mySecondParty = myFirstParty.copy()
print(myFirstParty.partyPets[0].health)
mySecondParty.partyPets[0].health -= 100
print(myFirstParty.partyPets[0].health)
