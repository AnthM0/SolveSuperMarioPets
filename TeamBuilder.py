from SolveSuperMarioPets.BattleSim import *
from SolveSuperMarioPets.Party import *

roundOneTeams = [
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
    [Otter(), Ant(), Fish(3, 4)]
]

roundTwoTeams = [
    [Ant(), Ant(), Ant(), Fish(3, 4), Fish()],
    [Mosquito(5, 5), Fish(), Otter(2, 3), Cricket()]
]

roundThreeTeams = [
    [Ant(5, 4, 2), Sheep(), Kangaroo(2, 3), Fish(4, 5, 2), Hedgehog(4, 3)],
    [Otter(2, 3, 1, MeatBone()), Fish(), Turtle(), Ant(5, 4, 2), Duck(2, 4)]
]

roundFourTeams = [

]

roundFiveTeams = [

]

roundSixTeams = [

]

roundSevenTeams = [

]

roundEightTeams = [

]

roundNineTeams = [

]

roundTenTeams = [

]

roundElevenTeams = [

]

roundTwelveTeams = [

]

roundThirteenTeams = [

]

roundFourteenTeams = [

]

roundFifteenTeams = [

]

roundSixteenTeams = [

]

roundSeventeenTeams = [

]

roundEighteenTeams = [

]

roundNineteenTeams = [

]

roundTwentyTeams = [

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

# myParty = Party(roundOneTeams[13])
# one_vs_many(myParty, roundOneTeams, 100000, match_up)
# print(len(roundOneTeams))
read_results_array(many_vs_many(roundOneTeams, 100000, match_up, False))


# myPets = [Sheep(item=Mushroom())]
# otherPets = [Mammoth()]
# myParty = Party(myPets)
# otherParty = Party(otherPets)
# Simulator.single_battle(myParty, otherParty, True)
# Simulator.multi_battle(myParty, otherParty, 100000)

with open('match_up_dict.pkl', 'wb') as f:
    pickle.dump(match_up, f)
