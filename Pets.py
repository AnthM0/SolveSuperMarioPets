import random
from SolveSuperMarioPets.OtherFunctions import *

#
# Missing Elephant, Hedgehog, Spider
# Missing Badger, Blowfish, Camel
# Missing Hippo
# Missing Rhino
# Missing Fly, Gorilla, Tiger


class Pet:
    def __init__(self, attack, health, level, item, name):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
        self.item = item
    def copy(self):
        return Pet(self.attack, self.health, self.level, self.item, self.name)
    def print(self):
        print(self.name, "(", self.attack, ",", self.health, ")   ", sep="", end="")

    def boost(self, additions):
        self.attack += additions[0]
        self.health += additions[1]
    def take_damage(self, damage, party, other_party):
        self.health -= damage

    def start_battle(self, party, other_party):
        return False
    def before_attack(self, party, other_party):
        return False
    def make_attack(self, my_party, other_party):
        other_party.partyPets[0].take_damage(self.attack, my_party, other_party)
    def after_attack(self, location, party, other_party):
        return False
    def faint_damage(self, location, party, other_party):
        return False
    def faint(self, location, party, other_party):
        return
    def friend_has_fainted(self, number, prev_party, n_party):
        return
    def new_pet_spawning(self, new_pet):
        return


# Tier One Pets ##
class Ant(Pet):
    def __init__(self, attack=2, health=1, level=1, item=None, name="Ant"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Ant(self.attack, self.health, self.level, self.item, self.name)
    def faint(self, location, party, other_party):
        party.partyPets[random.randint(0, party.len()-1)].boost([2*self.level, self.level])


class Beaver(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Beaver"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Beaver(self.attack, self.health, self.level, self.item, self.name)


class Cricket(Pet):
    def __init__(self, attack=1, health=2, level=1, item=None, name="Cricket"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Cricket(self.attack, self.health, self.level, self.item, self.name)
    def faint(self, location, party, other_party):
        spawns = [ZCricket(self.level, self.level, self.level)]
        party.spawn(spawns, location)


class Duck(Pet):
    def __init__(self, attack=1, health=3, level=1, item=None, name="Duck"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Duck(self.attack, self.health, self.level, self.item, self.name)


class Fish(Pet):
    def __init__(self, attack=2, health=3, level=1, item=None, name="Fish"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Fish(self.attack, self.health, self.level, self.item, self.name)


class Horse(Pet):
    def __init__(self, attack=2, health=1, level=1, item=None, name="Horse"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Horse(self.attack, self.health, self.level, self.item, self.name)
    def new_pet_spawning(self, new_pet):
        new_pet.boost([self.level, 0])


class Mosquito(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Mosquito"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Mosquito(self.attack, self.health, self.level, self.item, self.name)
    def start_battle(self, party, other_party):
        selections = random.sample(range(0, other_party.len()), min(self.level, other_party.len()))
        for i in selections:
            other_party.partyPets[i].take_damage(1, other_party, party)
        return True


class Otter(Pet):
    def __init__(self, attack=1, health=2, level=1, item=None, name="Otter"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Otter(self.attack, self.health, self.level, self.item, self.name)


class Pig(Pet):
    def __init__(self, attack=3, health=1, level=1, item=None, name="Pig"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Pig(self.attack, self.health, self.level, self.item, self.name)


class ZCricket(Pet):
    def __init__(self, attack=1, health=1, level=1, item=None, name="ZCricket"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return ZCricket(self.attack, self.health, self.level, self.item, self.name)


class Bee(Pet):
    def __init__(self, attack=1, health=1, level=1, item=None, name="Bee"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Bee(self.attack, self.health, self.level, self.item, self.name)


# Tier Two Pets
# Missing Elephant, Hedgehog, Rat, Spider, Flamingo
class Crab(Pet):
    def __init__(self, attack=3, health=3, level=1, item=None, name="Crab"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Crab(self.attack, self.health, self.level, self.item, self.name)


class Dodo(Pet):
    def __init__(self, attack=2, health=3, level=1, item=None, name="Dodo"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Dodo(self.attack, self.health, self.level, self.item, self.name)
    def start_battle(self, party, other_party):
        if party.position(self) != 0:
            party.partyPets[party.position(self) - 1].boost([int((self.attack+1)/2*self.level), 0])
        return False


class Elephant(Pet):
    def __init__(self, attack=3, health=5, level=1, item=None, name="Elephant"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Elephant(self.attack, self.health, self.level, self.item, self.name)
    def before_attack(self, party, otherParty):
        if party.position(self) == 0 and party.len() > 1:
            party.partyPets[1].take_damage(1, party, otherParty)
            if party.len() > 2 and self.level > 1:
                party.partyPets[2].take_damage(1, party, otherParty)
                if party.len() > 3 and self.level > 2:
                    party.partyPets[3].take_damage(1, party, otherParty)
            return True
        return False


class Flamingo(Pet):
    def __init__(self, attack=3, health=1, level=1, item=None, name="Flamingo"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Flamingo(self.attack, self.health, self.level, self.item, self.name)
    def faint(self, location, party, other_party):
        if location < party.len():
            party.partyPets[location].boost([self.level, self.level])
        if (location+1) < party.len():
            party.partyPets[location+1].boost([self.level, self.level])


class Peacock(Pet):
    def __init__(self, attack=1, health=5, level=1, item=None, name="Peacock"):
        self.abilityUses = self.level
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Peacock(self.attack, self.health, self.level, self.item, self.name)
    def take_damage(self, damage, party, otherParty):
        if damage > 0 and self.abilityUses > 0:
            self.attack += int((self.attack+1)/2)
            self.abilityUses -= 1
        super().take_damage(damage, party, otherParty)


class Rat(Pet):
    def __init__(self, attack=4, health=5, level=1, item=None, name="Rat"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Rat(self.attack, self.health, self.level, self.item, self.name)
    def faint(self, location, party, other_party):
        spawns = []
        for i in range(0, self.level):
            spawns.append(DirtyRat(1, 1, self.level))
        other_party.spawn(spawns, 0)


class Shrimp(Pet):
    def __init__(self, attack=2, health=3, level=1, item=None, name="Shrimp"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Shrimp(self.attack, self.health, self.level, self.item, self.name)


class Swan(Pet):
    def __init__(self,attack=1,health=3,level=1,item=None,name="Swan"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Swan(self.attack, self.health, self.level, self.item, self.name)


class DirtyRat(Pet):
    def __init__(self, attack=1, health=1, level=1, item=None, name="DirtyRat"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return DirtyRat(self.attack, self.health, self.level, self.item, self.name)


# Tier Three Pets ##
# Missing Badger, Blowfish, Camel
class Dog(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Dog"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Dog(self.attack, self.health, self.level, self.item, self.name)
    def new_pet_spawning(self, new_pet):
        if random.randint(0, 1) == 0:
            self.attack += self.level
        else:
            self.health += self.level


class Giraffe(Pet):
    def __init__(self, attack=2, health=5, level=1, item=None, name="Giraffe"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Giraffe(self.attack, self.health, self.level, self.item, self.name)


class Kangaroo(Pet):
    def __init__(self, attack=2, health=5, level=1, item=None, name="Kangaroo"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Kangaroo(self.attack, self.health, self.level, self.item, self.name)
    def after_attack(self, location, party, other_party):
        if location == 1:
            self.boost([2*self.level, 2*self.level])
        return False


class Ox(Pet):
    def __init__(self, attack=1, health=4, level=1, item=None, name="Ox"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Ox(self.attack, self.health, self.level, self.item, self.name)
    def friend_has_fainted(self, number, prev_party, n_party):
        old_position = prev_party.position(self)
        new_position = n_party.position(self)
        if old_position > 0:
            if new_position == 0:
                self.boost([2*self.level, 0])
            elif prev_party.partyPets[old_position-1] != n_party.partyPets[new_position-1]:
                self.boost([2 * self.level, 0])



class Rabbit(Pet):
    def __init__(self, attack=3, health=2, level=1, item=None, name="Rabbit"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Rabbit(self.attack, self.health, self.level, self.item, self.name)


class Sheep(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Sheep"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Sheep(self.attack, self.health, self.level, self.item, self.name)
    def faint(self, location, party, other_party):
        spawns = [Ram(2*self.level, 2*self.level, self.level), Ram(2*self.level, 2*self.level, self.level)]
        party.spawn(spawns, location)


class Snail(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Snail"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Snail(self.attack, self.health, self.level, self.item, self.name)


class Turtle(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Turtle"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Turtle(self.attack, self.health, self.level, self.item, self.name)


class Ram(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Ram"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Ram(self.attack, self.health, self.level, self.item, self.name)


# Tier Four Pets ##
# Missing Hippo
class Whale(Pet):
    def __init__(self, attack=3, health=8, level=1, item=None, name="Whale"):
        self.stored_pet = None
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Whale(self.attack, self.health, self.level, self.item, self.name)
    def faint(self, location, party, other_party):
        party.spawn([self.stored_pet], location)
    def start_battle(self, party, other_party):
        if party.position(self) != 0:
            target_pet = party.partyPets[party.position(self)-1]
            self.stored_pet = target_pet.copy()
            self.stored_pet.attack = 1
            self.stored_pet.health = 1
            target_pet.health = 0
        return True


class Bison(Pet):
    def __init__(self, attack=6, health=6, level=1, item=None, name="Bison"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Bison(self.attack, self.health, self.level, self.item, self.name)


class Deer(Pet):
    def __init__(self, attack=1, health=1, level=1, item=None, name="Deer"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Deer(self.attack, self.health, self.level, self.item, self.name)
    def faint(self, location, party, other_party):
        spawns = [Bus(5*self.level, 5*self.level, self.level)]
        party.spawn(spawns, location)


class Dolphin(Pet):
    def __init__(self, attack=4, health=6, level=1, item=None, name="Dolphin"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Dolphin(self.attack, self.health, self.level, self.item, self.name)
    def start_battle(self, party, other_party):
        other_party.low_health_pet().take_damage(5*self.level, other_party, party)
        return True


class Penguin(Pet):
    def __init__(self, attack=1, health=2, level=1, item=None, name="Penguin"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Penguin(self.attack, self.health, self.level, self.item, self.name)


class Rooster(Pet):
    def __init__(self, attack=5, health=3, level=1, item=None, name="Rooster"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Rooster(self.attack, self.health, self.level, self.item, self.name)
    def faint(self, location, party, other_party):
        chick_attack = int((self.attack+1)/2)
        spawns = []
        for i in range(0, self.level):
            spawns.append(Chick(chick_attack, 1, self.level))
        party.spawn(spawns, location)


class Skunk(Pet):
    def __init__(self, attack=3, health=6, level=1, item=None, name="Skunk"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Skunk(self.attack, self.health, self.level, self.item, self.name)
    def start_battle(self, party, other_party):
        high_health_pet = other_party.high_health_pet()
        high_health_pet.health = int((high_health_pet.health*(3-self.level)/3)+1)
        return False


class Squirrel(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Squirrel"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Squirrel(self.attack, self.health, self.level, self.item, self.name)


class Worm(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Worm"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Worm(self.attack, self.health, self.level, self.item, self.name)


class Bus(Pet):
    def __init__(self, attack=5, health=5, level=1, item=None, name="Bus"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Bus(self.attack, self.health, self.level, self.item, self.name)


class Chick(Pet):
    def __init__(self, attack=3, health=1, level=1, item=None, name="Chick"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Chick(self.attack, self.health, self.level, self.item, self.name)


# Tier Five Pets ##
# Missing Rhino
class Monkey(Pet):
    def __init__(self, attack=1, health=2, level=1, item=None, name="Monkey"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Monkey(self.attack, self.health, self.level, self.item, self.name)


class Cow(Pet):
    def __init__(self, attack=4, health=6, level=1, item=None, name="Cow"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Cow(self.attack, self.health, self.level, self.item, self.name)


class Crocodile(Pet):
    def __init__(self, attack=8, health=4, level=1, item=None, name="Crocodile"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Crocodile(self.attack, self.health, self.level, self.item, self.name)
    def start_battle(self, party, other_party):
        damage = arrZeros(other_party.len())
        damage[-1] = 8*self.level
        other_party.take_damage(damage, party)
        return True


class Scorpion(Pet):
    def __init__(self, attack=1, health=1, level=1, item=None, name="Scorpion"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Scorpion(self.attack, self.health, self.level, self.item, self.name)


class Seal(Pet):
    def __init__(self, attack=3, health=8, level=1, item=None, name="Seal"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Seal(self.attack, self.health, self.level, self.item, self.name)


class Shark(Pet):
    def __init__(self, attack=4, health=4, level=1, item=None, name="Shark"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Shark(self.attack, self.health, self.level, self.item, self.name)
    def friend_has_fainted(self, number, prev_party, n_party):
        self.boost([2*self.level*number, self.level*number])


class Turkey(Pet):
    def __init__(self, attack=3, health=4, level=1, item=None, name="Turkey"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Turkey(self.attack, self.health, self.level, self.item, self.name)
    def new_pet_spawning(self, new_pet):
        new_pet.boost([3*self.level, 3*self.level])


# Tier Six Pets ##
# Missing Fly, Gorilla, Tiger
class Cat(Pet):
    def __init__(self, attack=4, health=5, level=1, item=None, name="Cat"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Cat(self.attack, self.health, self.level, self.item, self.name)


class Boar(Pet):
    def __init__(self, attack=8, health=6, level=1, item=None, name="Boar"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Boar(self.attack, self.health, self.level, self.item, self.name)
    def before_attack(self, party, otherParty):
        self.boost([2*self.level, 2*self.level])
        return False


class Dragon(Pet):
    def __init__(self, attack=6, health=8, level=1, item=None, name="Dragon"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Dragon(self.attack, self.health, self.level, self.item, self.name)


class Leopard(Pet):
    def __init__(self, attack=10, health=4, level=1, item=None, name="Leopard"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Leopard(self.attack, self.health, self.level, self.item, self.name)
    def start_battle(self, party, other_party):
        damage = arrZeros(other_party.len())
        selections = random.sample(range(0, other_party.len()), min(self.level, other_party.len()))
        for i in selections:
            damage[i] = int((self.attack+1)/2)
        other_party.take_damage(damage, party)
        return True


class Mammoth(Pet):
    def __init__(self, attack=3, health=10, level=1, item=None, name="Mammoth"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Mammoth(self.attack, self.health, self.level, self.item, self.name)
    def faint(self, location, party, other_party):
        for pet in party.partyPets:
            pet.boost([2*self.level, 2*self.level])


class Snake(Pet):
    def __init__(self, attack=6, health=6, level=1, item=None, name="Snake"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return Snake(self.attack, self.health, self.level, self.item, self.name)
    def after_attack(self, location, party, other_party):
        if location == 1:
            other_party.partyPets[random.randint(0, other_party.len() - 1)].take_damage(5*self.level, party, other_party)
            return True
        return False


class ZFly(Pet):
    def __init__(self, attack=5, health=5, level=1, item=None, name="ZFly"):
        super().__init__(attack, health, level, item, name)
    def copy(self):
        return ZFly(self.attack, self.health, self.level, self.item, self.name)