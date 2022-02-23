from SolveSuperMarioPets.BattleSim import *
from SolveSuperMarioPets.Party import *

round_1_teams = [
    [Ant(), Ant(), Fish()],
    [Fish(), Fish(), Fish()],
    [Ant(), Ant(), Cricket()],
    [Mosquito(), Mosquito(), Mosquito()],
    [Fish(), Fish(), Mosquito()],
    [Cricket(2), Cricket(2), Horse()],
    [Otter(2, 3), Fish(4, 5)],
    [Otter(), Otter(), Fish(4, 5)],
    [Ant(), Ant(), Mosquito()],
    [Ant(), Mosquito(), Mosquito()],
    [Ant(), Fish(), Fish()],
    [Ant(), Fish(3, 4), Otter()],
    [Otter(2, 3), Pig(5, 3)],
    [Otter(), Ant(), Fish(3, 4)],
    [Ant(), Beaver(), Beaver()],
    [Ant(4, 3), Otter(2, 3)]
]

round_2_teams = [
    [Ant(), Ant(), Ant(), Fish(3, 4), Fish()],
    [Mosquito(5, 5), Fish(), Otter(2, 3), Cricket()],
    [Ant(), Ant(), Beaver(3, 3), Beaver(), Fish(2, 3)],
    [Horse(), Beaver(), Cricket(4, 5)]
]

round_3_teams = [
    [Ant(5, 4, 2), Sheep(), Kangaroo(2, 3), Fish(4, 5, 2), Hedgehog(4, 3)],
    [Otter(2, 3, 1, MeatBone()), Fish(), Turtle(), Ant(5, 4, 2), Duck(2, 4)],
    [Ant(3, 2), Rat(5, 6), Sheep(), Beaver(4, 4), Fish()]
]

round_4_teams = [

]

round_5_teams = [

]

round_6_teams = [

]

round_7_teams = [

]

round_8_teams = [

]

round_9_teams = [

]

round_10_teams = [

]

round_11_teams = [

]

round_12_teams = [

]

round_13_teams = [
    [Hippo(20, 33, 2, Steak()), Snake(7, 7), Monkey(), Bison(17, 17, 2), Badger(9, 8, 1, Honey())]
]

round_14_teams = [

]

round_15_teams = [

]

round_16_teams = [

]

round_17_teams = [

]

round_18_teams = [

]

round_19_teams = [

]

round_20_teams = [

]


def one_vs_many(my_party, other_party_list, tests, match_up_dictionary=None, printing=True):
    if printing:
        my_party.printF()
        print("\n")
    comparisons = []
    points = 0
    win_value = 3
    tie_value = 1
    for other_party_pets in other_party_list:
        other_party = Party(other_party_pets)
        if printing:
            other_party.printF()
            print()
        cur_results = Simulator.multi_battle(my_party, other_party, tests, match_up_dictionary, False, printing)
        comparisons.append([other_party, cur_results])
        points += cur_results[0]*win_value + cur_results[1]*tie_value
        if printing:
            print()
    if printing:
        print("\n")
        my_party.printF()
        print("\n", "Points: ", points)
    return points


def many_vs_many(party_lists, tests, match_up_dictionary=None, printing=False):
    result_array = []
    for my_party_pets in party_lists:
        my_party = Party(my_party_pets)
        results = one_vs_many(my_party, party_lists, tests, match_up_dictionary, False)
        result_array.append([my_party, results])
        if printing:
            my_party.printF()
            print(":", int(results))
    return result_array


def read_results_array(results_array):
    while len(results_array) > 0:
        highest = results_array[0]
        highest_score = results_array[0][1]
        for i in range(1, len(results_array)):
            current = results_array[i]
            if current[1] > highest_score:
                highest = current
                highest_score = current[1]
        print(int(highest_score), " : ", end="")
        highest[0].printF()
        print()
        results_array.remove(highest)


with open('match_up_dict.pkl', 'rb') as f:
    match_up = pickle.load(f)

myParty = Party(round_1_teams[13])
# one_vs_many(myParty, round_1_teams, 100000, match_up)
# print(len(round_1_teams))
# read_results_array(many_vs_many(round_1_teams, 100000, match_up, False))


# myPets = [Deer(5, 5, 2), Whale(4, 9, 1, Chili()), Tiger(9, 8, 2), Turkey(5, 6, 2), Turkey(11, 8, 2, Melon(), "Parrot")]
# otherPets = [Hippo(20, 33, 2, Steak()), Snake(7, 7), Monkey(), Bison(17, 17, 2), Badger(9, 8, 1, Honey())]
myPets = [Hippo(), Snake()]
otherPets = [Giraffe(), Swan()]
myParty = Party(myPets)
otherParty = Party(otherPets)
Simulator.single_battle(myParty, otherParty, True)
# Simulator.multi_battle(myParty, otherParty, 100000)

with open('match_up_dict.pkl', 'wb') as f:
    pickle.dump(match_up, f)
