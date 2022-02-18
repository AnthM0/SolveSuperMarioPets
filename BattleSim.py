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
