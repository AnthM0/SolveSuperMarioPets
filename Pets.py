import random
from OtherFunctions import *

#
# Missing Dodo, Elephant, Hedgehog, Rat, Spider
# Missing Badger, Blowfish, Camel, Kangaroo, Ox, Turtle
# Missing Whale, Hippo, Skunk
# Missing Rhino
# Missing Boar, Fly, Gorilla, Snake, Tiger


class Pet:
    def __init__(self,attack,health,level,name):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Pet(self.attack, self.health, self.name, self.level)
    def addToParty(self,party):
        self.party = party
    def print(self):
        print(self.name,"(",self.attack,",",self.health,")   ",sep="",end="")

    def boost(self, additions):
        self.attack += additions[0]
        self.health += additions[1]
    def boostFromFaint(self, additions):
        self.boost(additions)

    def takeDamage(self,damage):
        self.health -= damage
    def getAttack(self,lenOtherParty,position):
        damageArr = arrZeros(lenOtherParty)
        if(position == 0):
            damageArr[0] += self.attack
        return damageArr

    def startBattleDamage(self, lenOtherParty, lowHealthIndex):
        return arrZeros(lenOtherParty)

    def faintBoost(self,length):
        return arrZeros(length,[0,0])
    def faintSpawn(self):
        return []
    def faintDamage(self,location,lenParty,lenOtherParty):
        return [False,arrZeros(lenOtherParty,0),arrZeros(lenParty,0)]

    def petSpawned(self):
        return [0,0]


## Tier One Pets ##
class Ant(Pet):
    def __init__(self,attack=2,health=1,level=1,name="Ant"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Ant(self.attack, self.health, self.name, self.level)
    def faintBoost(self,length):
        boosts = arrZeros(length,[0,0])
        boosts[random.randint(0, length - 1)] = [2*self.level, self.level]
        return boosts

class Beaver(Pet):
    def __init__(self,attack=2,health=2,level=1,name="Beaver"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Beaver(self.attack, self.health, self.name, self.level)

class Cricket(Pet):
    def __init__(self,attack=1,health=2,level=1,name="Cricket"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Cricket(self.attack, self.health, self.name, self.level)
    def faintSpawn(self):
        return [ZCricket(self.level,self.level,self.level)]

class Duck(Pet):
    def __init__(self,attack=1,health=3,level=1,name="Duck"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Duck(self.attack, self.health, self.name, self.level)

class Fish(Pet):
    def __init__(self,attack=2,health=3,level=1,name="Fish"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Fish(self.attack, self.health, self.name, self.level)

class Horse(Pet):
    def __init__(self,attack=2,health=1,level=1,name="Horse"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Horse(self.attack, self.health, self.name, self.level)
    def petSpawned(self):
        return [self.level,0]

class Mosquito(Pet):
    def __init__(self,attack=2,health=2,level=1,name="Mosquito"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Mosquito(self.attack, self.health, self.name, self.level)
    def startBattleDamage(self, lenOtherParty, lowHealthIndex):
        damage = arrZeros(lenOtherParty)
        selections = random.sample(range(0,lenOtherParty), min(self.level,lenOtherParty))
        for i in selections:
            damage[i] = 1
        return damage

class Otter(Pet):
    def __init__(self,attack=1,health=2,level=1,name="Otter"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Otter(self.attack, self.health, self.name, self.level)

class Pig(Pet):
    def __init__(self,attack=3,health=1,level=1,name="Pig"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Pig(self.attack, self.health, self.name, self.level)

class ZCricket(Pet):
    def __init__(self,attack=1,health=1,level=1,name="ZCricket"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return ZCricket(self.attack, self.health, self.name, self.level)

class Bee(Pet):
    def __init__(self,attack=1,health=1,level=1,name="Bee"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Bee(self.attack, self.health, self.name, self.level)


## Tier Two Pets ##
## Missing Dodo, Elephant, Hedgehog, Rat, Spider
class Crab(Pet):
    def __init__(self,attack=3,health=3,level=1,name="Crab"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Crab(self.attack, self.health, self.name, self.level)

class Flamingo(Pet):
    def __init__(self,attack=3,health=1,level=1,name="Flamingo"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Flamingo(self.attack, self.health, self.name, self.level)
    def faintBoost(self, length):
        boosts = arrZeros(length, [0, 0])
        if(len(boosts) > 0):
            boosts[0] = [self.level, self.level]
            if(len(boosts) > 1):
                boosts[1] = [self.level, self.level]
        return boosts

class Peacock(Pet):
    def __init__(self,attack=1,health=5,level=1,name="Peacock"):
        self.name = name
        self.attack = attack
        self.health = health
        self.abilityUses = self.level
    def copy(self):
        return Peacock(self.attack, self.health, self.name, self.level)
    def takeDamage(self,damage):
        if(damage > 0 and self.abilityUses > 0):
            self.attack += int((self.attack+1)/2)
            self.abilityUses -= 1
        self.health -= damage

class Shrimp(Pet):
    def __init__(self,attack=2,health=3,level=1,name="Shrimp"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Shrimp(self.attack, self.health, self.name, self.level)

class Swan(Pet):
    def __init__(self,attack=1,health=3,level=1,name="Swan"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Swan(self.attack, self.health, self.name, self.level)

class DirtyRat(Pet):
    def __init__(self,attack=1,health=1,level=1,name="DirtyRat"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return DirtyRat(self.attack, self.health, self.name, self.level)


## Tier Three Pets ##
## Missing Badger, Blowfish, Camel, Kangaroo, Ox, Turtle
class Dog(Pet):
    def __init__(self,attack=2,health=2,level=1,name="Dog"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Dog(self.attack, self.health, self.name, self.level)
    def petSpawned(self):
        if(random.randint(0,1) == 0):
            self.attack += 1*self.level
        else:
            self.health += 1*self.level
        return [0,0]

class Giraffe(Pet):
    def __init__(self,attack=2,health=5,level=1,name="Giraffe"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Giraffe(self.attack, self.health, self.name, self.level)

class Rabbit(Pet):
    def __init__(self,attack=3,health=2,level=1,name="Rabbit"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Rabbit(self.attack, self.health, self.name, self.level)

class Sheep(Pet):
    def __init__(self,attack=2,health=2,level=1,name="Sheep"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Sheep(self.attack, self.health, self.name, self.level)
    def faintSpawn(self):
        return [Ram(2*self.level), Ram(2*self.level)]

class Snail(Pet):
    def __init__(self,attack=2,health=2,level=1,name="Snail"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Snail(self.attack, self.health, self.name, self.level)

class Ram(Pet):
    def __init__(self,attack=2,health=2,level=1,name="Ram"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Ram(self.attack, self.health, self.name, self.level)


## Tier Four Pets ##
## Missing Whale, Hippo, Skunk,
class Bison(Pet):
    def __init__(self,attack=6,health=6,level=1,name="Bison"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Bison(self.attack, self.health, self.name, self.level)

class Deer(Pet):
    def __init__(self,attack=1,health=1,level=1,name="Deer"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Deer(self.attack, self.health, self.name, self.level)
    def faintSpawn(self):
        return [Bus(5*self.level,5*self.level,self.level)]

class Dolphin(Pet):
    def __init__(self,attack=4,health=6,level=1,name="Dolphin"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Dolphin(self.attack, self.health, self.name, self.level)
    def startBattleDamage(self, lenOtherParty,lowHealthIndex):
        damage = arrZeros(lenOtherParty)
        damage[lowHealthIndex] = 5*self.level
        return damage

class Penguin(Pet):
    def __init__(self,attack=1,health=2,level=1,name="Penguin"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Penguin(self.attack, self.health, self.name, self.level)

class Rooster(Pet):
    def __init__(self,attack=5,health=3,level=1,name="Rooster"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Rooster(self.attack, self.health, self.name, self.level)
    def faintSpawn(self):
        chickAttack = int(self.attack/2)
        chickArr = []
        for i in range(0,self.level):
            chickArr.append(Chick(chickAttack,1,self.level))
        return chickArr

class Squirrel(Pet):
    def __init__(self,attack=2,health=2,level=1,name="Squirrel"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Squirrel(self.attack, self.health, self.name, self.level)

class Worm(Pet):
    def __init__(self,attack=2,health=2,level=1,name="Worm"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Worm(self.attack, self.health, self.name, self.level)

class Bus(Pet):
    def __init__(self,attack=5,health=5,level=1,name="Bus"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Bus(self.attack, self.health, self.name, self.level)

class Chick(Pet):
    def __init__(self,attack=3,health=1,level=1,name="Chick"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Chick(self.attack, self.health, self.name, self.level)

## Tier Five Pets ##
## Missing Rhino
class Monkey(Pet):
    def __init__(self,attack=1,health=2,level=1,name="Monkey"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Monkey(self.attack, self.health, self.name, self.level)

class Cow(Pet):
    def __init__(self,attack=4,health=6,level=1,name="Cow"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Cow(self.attack, self.health, self.name, self.level)

class Crocodile(Pet):
    def __init__(self,attack=8,health=4,level=1,name="Crocodile"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Crocodile(self.attack, self.health, self.name, self.level)
    def startBattleDamage(self, lenOtherParty, lowHealthIndex):
        damage = arrZeros(lenOtherParty)
        damage[lenOtherParty-1] = 8*self.level
        print(damage)
        return damage

class Scorpion(Pet):
    def __init__(self,attack=1,health=1,level=1,name="Scorpion"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Scorpion(self.attack, self.health, self.name, self.level)

class Seal(Pet):
    def __init__(self,attack=3,health=8,level=1,name="Seal"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Seal(self.attack, self.health, self.name, self.level)

class Shark(Pet):
    def __init__(self,attack=4,health=4,level=1,name="Shark"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Shark(self.attack, self.health, self.name, self.level)
    def boostFromFaint(self, additions):
        self.attack += additions[0] + 2*self.level
        self.health += additions[1] + self.level

class Turkey(Pet):
    def __init__(self,attack=3,health=4,level=1,name="Turkey"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Turkey(self.attack, self.health, self.name, self.level)
    def petSpawned(self):
        return [3*self.level,3*self.level]


## Tier Six Pets ##
## Missing Boar, Fly, Gorilla, Snake, Tiger
class Cat(Pet):
    def __init__(self,attack=4,health=5,level=1,name="Cat"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Cat(self.attack, self.health, self.name, self.level)

class Dragon(Pet):
    def __init__(self,attack=6,health=8,level=1,name="Dragon"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Dragon(self.attack, self.health, self.name, self.level)

class Leopard(Pet):
    def __init__(self,attack=10,health=4,level=1,name="Leopard"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Leopard(self.attack, self.health, self.name, self.level)
    def startBattleDamage(self, lenOtherParty, lowHealthIndex):
        damage = arrZeros(lenOtherParty)
        selections = random.sample(range(0, lenOtherParty), min(self.level, lenOtherParty))
        for i in selections:
            damage[i] = int((self.attack+1)/2)
        return damage

class Mammoth(Pet):
    def __init__(self,attack=3,health=10,level=1,name="Mammoth"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return Mammoth(self.attack, self.health, self.name, self.level)
    def faintBoost(self,length):
        boosts = arrZeros(length,[2*self.level,2*self.level])
        return boosts

class ZFly(Pet):
    def __init__(self,attack=5,health=5,level=1,name="ZFly"):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
    def copy(self):
        return ZFly(self.attack, self.health, self.name, self.level)