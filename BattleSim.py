from SolveSuperMarioPets.Pets import *
from SolveSuperMarioPets.Party import *
from SolveSuperMarioPets.Battle import *


class Simulator:
    def __init__(self, myPets=Party([Fish()]), otherPets=Party([Fish()])):
        self.myParty = myPets
        self.otherParty = otherPets

    @staticmethod
    def single_battle(self, myParty, otherParty, printing=True):
        thisBattle = Battle(myParty, otherParty)
        if printing:
            thisBattle.print_battle()
            print("       ...Pre Battle...")
        thisBattle.start_battle(printing)
        if printing:
            thisBattle.printBattle()
            print("       ...Start Battle...")
        outcome = thisBattle.checkOutcome()
        while outcome == 69:
            thisBattle.singleAttack()
            if printing:
                thisBattle.printBattle()
            outcome = thisBattle.checkOutcome()
        if printing:
            if outcome == 1:
                print("You Win!")
            elif outcome == -1:
                print("You Lost...")
            else:
                print("You Tied.")
        return outcome

    def multi_battle(self, tests):
        wins = 0
        ties = 0
        losses = 0
        for i in range(0, tests):
            myPetsParty = Party(self.myParty.copy())
            otherPetsParty = Party(self.otherParty.copy())
            outcome = self.runSingleBattle(myPetsParty, otherPetsParty, False)
            if outcome == 1:
                wins += 1
            elif outcome == -1:
                losses += 1
            else:
                ties += 1
        win_p = wins*100 / tests
        tie_p = ties*100 / tests
        loss_p = losses*100 / tests
        print("Win(", win_p, "%), Tie(", tie_p, "%), Loss(", loss_p, "%)")


myPets = [Elephant(), Mammoth(), Mammoth(), Mammoth()]
otherPets = [Mammoth(), Mammoth()]
myParty = Party(myPets)
otherParty = Party(otherPets)

myBattle = Battle(myParty, otherParty)
myBattle.start_battle(True)
myBattle.before_attack(True)
myBattle.make_attack(True)
myBattle.after_attack(True)


# battleSim = Simulator(myParty, otherParty)
# battleSim.single_battle(myParty, otherParty, True)
# battleSim.runMultiBattle(10000)

arr = [0, 2]