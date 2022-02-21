import random
from Pets import *
from Party import *
from Battle import *
from OtherFunctions import *

class Simulator:
    def __init__(self,myPets=Party([Fish()]),otherPets=Party([Fish()])):
        self.myParty = myPets
        self.otherParty = otherPets

    def runSingleBattle(self,myParty,otherParty,printing=True):
        thisBattle = Battle(myParty, otherParty)
        if(printing):
            thisBattle.printBattle()
            print("       ...Pre Battle...")
        thisBattle.startBattle()
        if(printing):
            thisBattle.printBattle()
            print("       ...Start Battle...")
        outcome = 69
        while outcome == 69:
            thisBattle.singleAttack()
            if(printing):
                thisBattle.printBattle()
            outcome = thisBattle.checkOutcome()
        if(printing):
            if(outcome == 1):
                print("You Win!")
            elif(outcome == -1):
                print("You Lost...")
            else:
                print("You Tied.")
        return outcome

    def runMultiBattle(self,tests):
        wins = 0
        ties = 0
        losses = 0
        for i in range(0,tests):
            myPetsParty = Party(self.myParty.copy())
            otherPetsParty = Party(self.otherParty.copy())
            outcome = self.runSingleBattle(myPetsParty, otherPetsParty, False)
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


myPets = [Dolphin()]
otherPets = [Mosquito(), Mammoth()]
myParty = Party(myPets)
otherParty = Party(otherPets)

battleSim = Simulator(myParty,otherParty)
battleSim.runSingleBattle(myParty, otherParty, True)
##battleSim.runMultiBattle(10000)
