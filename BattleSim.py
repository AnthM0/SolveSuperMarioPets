import pickle
from SolveSuperMarioPets.Pets import *
from SolveSuperMarioPets.Party import *
from SolveSuperMarioPets.Battle import *


class Simulator:
    def __init__(self, myPets=Party([Fish()]), otherPets=Party([Fish()])):
        self.myParty = myPets
        self.otherParty = otherPets

    @staticmethod
    def lookup(match_up, myParty, otherParty):
        myParty_str = myParty.hash_string()
        otherParty_str = otherParty.hash_string()
        if myParty_str in match_up.keys():
            if otherParty_str in match_up[myParty_str].keys():
                return match_up[myParty_str][otherParty_str]
        if otherParty_str in match_up.keys():
            if myParty_str in match_up[otherParty_str].keys():
                return match_up[otherParty_str][myParty_str]
        return []

    @staticmethod
    def load(match_up, myParty, otherParty, results):
        inverted_results = [results[2], results[1], results[0]]
        myParty_str = myParty.hash_string()
        otherParty_str = otherParty.hash_string()
        if myParty_str not in match_up.keys():
            match_up[myParty_str] = {}
        if otherParty_str not in match_up[myParty_str].keys():
            match_up[myParty_str][otherParty_str] = []
        if otherParty_str not in match_up.keys():
            match_up[otherParty_str] = {}
        if myParty_str not in match_up[otherParty_str].keys():
            match_up[otherParty_str][myParty_str] = []
        match_up[myParty_str][otherParty_str] = results
        match_up[otherParty_str][myParty_str] = inverted_results

    @staticmethod
    def single_battle(myParty, otherParty, printing=True):
        thisBattle = Battle(myParty, otherParty)
        if printing:
            thisBattle.print_battle()
        thisBattle.start_battle()
        if printing:
            print("       ...Pre Battle...")
            thisBattle.print_battle()
        outcome = thisBattle.outcome()
        while outcome == 69:
            if printing:
                print("       ...Before Attack...")
                thisBattle.print_battle()
            thisBattle.before_attack()
            outcome = thisBattle.outcome()
            if outcome == 69:
                thisBattle.make_attack()
                outcome = thisBattle.outcome()
                if printing:
                    print("       ... Attack...")
                    thisBattle.print_battle()
                if outcome == 69:
                    thisBattle.after_attack()
                    outcome = thisBattle.outcome()
                    if printing:
                        print("       ...After Attack...")
                        thisBattle.print_battle()
            if printing:
                print()
        if printing:
            if outcome == 1:
                print("You Win!")
            elif outcome == -1:
                print("You Lost...")
            else:
                print("You Tied.")
        return outcome

    @staticmethod
    def multi_battle(myParty, otherParty, tests, match_up=None, override=False, printing=True):
        if match_up is not None:
            outcome_array = Simulator.lookup(match_up, myParty, otherParty)
            if (len(outcome_array) > 0) and (not override):
                if printing:
                    print("Win(", outcome_array[0], "%), Tie(", outcome_array[1], "%), Loss(", outcome_array[2], "%)")
                return outcome_array
        wins = 0
        ties = 0
        losses = 0
        for i in range(0, tests):
            myPetsParty = Party(myParty.copy())
            otherPetsParty = Party(otherParty.copy())
            outcome = Simulator.single_battle(myPetsParty, otherPetsParty, False)
            if outcome == 1:
                wins += 1
            elif outcome == -1:
                losses += 1
            else:
                ties += 1
        win_p = wins*100 / tests
        tie_p = ties*100 / tests
        loss_p = losses*100 / tests
        if printing:
            print("Win(", win_p, "%), Tie(", tie_p, "%), Loss(", loss_p, "%)")
        if match_up is not None:
            Simulator.load(match_up, myParty, otherParty, [win_p, tie_p, loss_p])
        return [win_p, tie_p, loss_p]


# with open('match_up_dict.pkl', 'rb') as f:
#     match_up = pickle.load(f)

# Simulator.single_battle(myParty, otherParty, True)
# Simulator.multi_battle(myParty, otherParty, 100000)

# print(match_up)
# with open('match_up_dict.pkl', 'wb') as f:
#     pickle.dump(match_up, f)
