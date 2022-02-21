import random
from OtherFunctions import *

class Pet:
    def __init__(self,attack,health,name):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Pet(self.attack, self.health, self.name)
    def addToParty(self,party):
        self.party = party
    def boost(self, additions):
        self.attack += additions[0]
        self.health += additions[1]
    def boostFromFaint(self, additions):
        self.attack += additions[0]
        self.health += additions[1]
    def takeDamage(self,damage):
        self.health -= damage
    def getAttack(self,lenOtherParty,position):
        damageArr = arrZeros(lenOtherParty)
        if(position == 0):
            damageArr[0] += self.attack
        return damageArr
    def startBattle(self,lenOtherParty):
        return arrZeros(lenOtherParty)
    def print(self):
        print(self.name,"(",self.attack,",",self.health,")   ",sep="",end="")
    def faintBoost(self,length):
        return arrZeros(length,[0,0])
    def faintSpawn(self):
        return []
    def petSpawned(self):
        return [0,0]


## Tier One Pets ##
class Ant(Pet):
    def __init__(self,attack=2,health=1,name="Ant"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Ant(self.attack, self.health, self.name)
    def faintBoost(self,length):
        boosts = arrZeros(length,[0,0])
        boosts[random.randint(0, length - 1)] = [2,1]
        return boosts

class Beaver(Pet):
    def __init__(self,attack=2,health=2,name="Beaver"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Beaver(self.attack, self.health, self.name)

class Cricket(Pet):
    def __init__(self,attack=1,health=2,name="Cricket"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Cricket(self.attack, self.health, self.name)
    def faintSpawn(self):
        return [ZCricket()]

class Duck(Pet):
    def __init__(self,attack=1,health=3,name="Duck"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Duck(self.attack, self.health, self.name)

class Fish(Pet):
    def __init__(self,attack=2,health=3,name="Fish"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Fish(self.attack, self.health, self.name)

class Horse(Pet):
    def __init__(self,attack=2,health=1,name="Horse"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Horse(self.attack, self.health, self.name)
    def petSpawned(self):
        return [1,0]

class Mosquito(Pet):
    def __init__(self,attack=2,health=2,name="Mosquito"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Mosquito(self.attack, self.health, self.name)
    def startBattle(self,lenOtherParty):
        damage = arrZeros(lenOtherParty)
        damage[random.randint(0,lenOtherParty-1)] = 1
        return damage

class Otter(Pet):
    def __init__(self,attack=1,health=2,name="Otter"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Otter(self.attack, self.health, self.name)

class Pig(Pet):
    def __init__(self,attack=3,health=1,name="Pig"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Pig(self.attack, self.health, self.name)

class ZCricket(Pet):
    def __init__(self,attack=1,health=1,name="ZCricket"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return ZCricket(self.attack, self.health, self.name)

class Bee(Pet):
    def __init__(self,attack=1,health=1,name="Bee"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Bee(self.attack, self.health, self.name)


## Tier Two Pets ##
## Missing Dodo, Elephant, Hedgehog, Rat, Spider
class Crab(Pet):
    def __init__(self,attack=3,health=3,name="Crab"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Crab(self.attack, self.health, self.name)

class Flamingo(Pet):
    def __init__(self,attack=3,health=1,name="Flamingo"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Flamingo(self.attack, self.health, self.name)
    def faintBoost(self, length):
        boosts = arrZeros(length, [0, 0])
        if(len(boosts) > 0):
            boosts[0] = [1,1]
            if(len(boosts) > 1):
                boosts[1] = [1, 1]
        return boosts

class Hedgehog(Pet):
    def __init__(self,attack=3,health=2,name="Hedgehog"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Hedgehog(self.attack, self.health, self.name)

class Peacock(Pet):
    def __init__(self,attack=1,health=5,name="Peacock"):
        self.name = name
        self.attack = attack
        self.health = health
        self.abilityUses = 1
    def copy(self):
        return Peacock(self.attack, self.health, self.name)
    def takeDamage(self,damage):
        if(damage > 0 and self.abilityUses > 0):
            self.attack += int((self.attack+1)/2)
            self.abilityUses -= 1
        self.health -= damage

class Shrimp(Pet):
    def __init__(self,attack=2,health=3,name="Shrimp"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Shrimp(self.attack, self.health, self.name)

class Swan(Pet):
    def __init__(self,attack=1,health=3,name="Swan"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Swan(self.attack, self.health, self.name)

class DirtyRat(Pet):
    def __init__(self,attack=1,health=1,name="DirtyRat"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return DirtyRat(self.attack, self.health, self.name)


## Tier Three Pets ##
## Missing Badger, Blowfish, Camel, Kangaroo, Ox, Turtle
class Dog(Pet):
    def __init__(self,attack=2,health=2,name="Dog"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Dog(self.attack, self.health, self.name)
    def petSpawned(self):
        if(random.randint(0,1) == 0):
            self.attack += 1
        else:
            self.health += 1
        return [0,0]

class Giraffe(Pet):
    def __init__(self,attack=2,health=5,name="Giraffe"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Giraffe(self.attack, self.health, self.name)

class Rabbit(Pet):
    def __init__(self,attack=3,health=2,name="Rabbit"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Rabbit(self.attack, self.health, self.name)

class Sheep(Pet):
    def __init__(self,attack=2,health=2,name="Sheep"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Sheep(self.attack, self.health, self.name)
    def faintSpawn(self):
        return [Ram(), Ram()]

class Snail(Pet):
    def __init__(self,attack=2,health=2,name="Snail"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Snail(self.attack, self.health, self.name)

class Ram(Pet):
    def __init__(self,attack=2,health=2,name="Ram"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Ram(self.attack, self.health, self.name)


## Tier Four Pets ##
## Missing Whale, Dophin, Hippo, Skunk,
class Bison(Pet):
    def __init__(self,attack=6,health=6,name="Bison"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Bison(self.attack, self.health, self.name)

class Deer(Pet):
    def __init__(self,attack=1,health=1,name="Deer"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Deer(self.attack, self.health, self.name)
    def faintSpawn(self):
        return [ZCricket()]

class Penguin(Pet):
    def __init__(self,attack=1,health=2,name="Penguin"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Penguin(self.attack, self.health, self.name)

class Rooster(Pet):
    def __init__(self,attack=5,health=3,name="Rooster"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Rooster(self.attack, self.health, self.name)
    def faintSpawn(self):
        chickAttack = int(self.attack/2)
        return [Chick(chickAttack,1)]

class Squirrel(Pet):
    def __init__(self,attack=2,health=2,name="Squirrel"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Squirrel(self.attack, self.health, self.name)

class Worm(Pet):
    def __init__(self,attack=2,health=2,name="Worm"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Worm(self.attack, self.health, self.name)

class Bus(Pet):
    def __init__(self,attack=5,health=5,name="Bus"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Bus(self.attack, self.health, self.name)

class Chick(Pet):
    def __init__(self,attack=3,health=1,name="Chick"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Chick(self.attack, self.health, self.name)

## Tier Five Pets ##
## Missing Rhino
class Monkey(Pet):
    def __init__(self,attack=1,health=2,name="Monkey"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Monkey(self.attack, self.health, self.name)

class Cow(Pet):
    def __init__(self,attack=4,health=6,name="Cow"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Cow(self.attack, self.health, self.name)

class Crocodile(Pet):
    def __init__(self,attack=8,health=4,name="Crocodile"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Crocodile(self.attack, self.health, self.name)
    def startBattle(self,lenOtherParty):
        damage = arrZeros(lenOtherParty)
        damage[lenOtherParty-1] = 8
        print(damage)
        return damage

class Scorpion(Pet):
    def __init__(self,attack=1,health=1,name="Scorpion"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Scorpion(self.attack, self.health, self.name)

class Seal(Pet):
    def __init__(self,attack=3,health=8,name="Seal"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Seal(self.attack, self.health, self.name)

class Shark(Pet):
    def __init__(self, attack=4, health=4, name="Shark"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Shark(self.attack, self.health, self.name)
    def boostFromFaint(self, additions):
        self.attack += additions[0] + 2
        self.health += additions[1] + 1

class Turkey(Pet):
    def __init__(self,attack=3,health=4,name="Turkey"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Turkey(self.attack, self.health, self.name)
    def petSpawned(self):
        return [3,3]


## Tier Six Pets ##
## Missing Boar, Fly, Gorilla, Snake, Tiger
class Cat(Pet):
    def __init__(self,attack=4,health=5,name="Cat"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Cat(self.attack, self.health, self.name)

class Dragon(Pet):
    def __init__(self,attack=6,health=8,name="Dragon"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Dragon(self.attack, self.health, self.name)

class Leopard(Pet):
    def __init__(self,attack=10,health=4,name="Leopard"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Leopard(self.attack, self.health, self.name)
    def startBattle(self,lenOtherParty):
        damage = arrZeros(lenOtherParty)
        damage[random.randint(0,lenOtherParty-1)] = int(self.attack/2)
        return damage

class Mammoth(Pet):
    def __init__(self,attack=3,health=10,name="Mammoth"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Mammoth(self.attack, self.health, self.name)
    def faintBoost(self,length):
        boosts = arrZeros(length,[2,2])
        return boosts

class ZFly(Pet):
    def __init__(self,attack=5,health=5,name="ZFly"):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return ZFly(self.attack, self.health, self.name)