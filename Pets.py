import random
from SolveSuperMarioPets.OtherFunctions import *

#
# Missing Dodo, Elephant, Hedgehog, Rat, Spider
# Missing Badger, Blowfish, Camel, Kangaroo, Ox, Turtle
# Missing Whale, Hippo, Skunk
# Missing Rhino
# Missing Boar, Fly, Gorilla, Snake, Tiger


class Pet:
    def __init__(self,attack,health,level,item,name):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
        self.item = item
    def copy(self):
        return Pet(self.attack, self.health, self.level, self.item, self.name)
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
    def __init__(self,attack=2,health=1,level=1,item=None,name="Ant"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Ant(self.attack, self.health, self.level, self.item, self.name)
    def faintBoost(self,length):
        boosts = arrZeros(length,[0,0])
        boosts[random.randint(0, length)] = [2*self.level, self.level]
        return boosts

class Beaver(Pet):
    def __init__(self,attack=2,health=2,level=1,item=None,name="Beaver"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Beaver(self.attack, self.health, self.level, self.item, self.name)

class Cricket(Pet):
    def __init__(self,attack=1,health=2,level=1,item=None,name="Cricket"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Cricket(self.attack, self.health, self.level, self.item, self.name)
    def faintSpawn(self):
        return [ZCricket(self.level,self.level,self.level)]

class Duck(Pet):
    def __init__(self,attack=1,health=3,level=1,item=None,name="Duck"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Duck(self.attack, self.health, self.level, self.item, self.name)

class Fish(Pet):
    def __init__(self,attack=2,health=3,level=1,item=None,name="Fish"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Fish(self.attack, self.health, self.level, self.item, self.name)

class Horse(Pet):
    def __init__(self,attack=2,health=1,level=1,item=None,name="Horse"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Horse(self.attack, self.health, self.level, self.item, self.name)
    def petSpawned(self):
        return [self.level,0]

class Mosquito(Pet):
    def __init__(self,attack=2,health=2,level=1,item=None,name="Mosquito"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Mosquito(self.attack, self.health, self.level, self.item, self.name)
    def startBattleDamage(self, lenOtherParty, lowHealthIndex):
        damage = arrZeros(lenOtherParty)
        selections = random.sample(range(0,lenOtherParty), min(self.level,lenOtherParty))
        for i in selections:
            damage[i] = 1
        return damage

class Otter(Pet):
    def __init__(self,attack=1,health=2,level=1,item=None,name="Otter"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Otter(self.attack, self.health, self.level, self.item, self.name)

class Pig(Pet):
    def __init__(self,attack=3,health=1,level=1,item=None,name="Pig"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Pig(self.attack, self.health, self.level, self.item, self.name)

class ZCricket(Pet):
    def __init__(self,attack=1,health=1,level=1,item=None,name="ZCricket"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return ZCricket(self.attack, self.health, self.level, self.item, self.name)

class Bee(Pet):
    def __init__(self,attack=1,health=1,level=1,item=None,name="Bee"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Bee(self.attack, self.health, self.level, self.item, self.name)


## Tier Two Pets ##
## Missing Dodo, Elephant, Hedgehog, Rat, Spider
class Crab(Pet):
    def __init__(self,attack=3,health=3,level=1,item=None,name="Crab"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Crab(self.attack, self.health, self.level, self.item, self.name)

class Flamingo(Pet):
    def __init__(self,attack=3,health=1,level=1,item=None,name="Flamingo"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Flamingo(self.attack, self.health, self.level, self.item, self.name)
    def faintBoost(self, length):
        boosts = arrZeros(length, [0, 0])
        if(len(boosts) > 0):
            boosts[0] = [self.level, self.level]
            if(len(boosts) > 1):
                boosts[1] = [self.level, self.level]
        return boosts

class Peacock(Pet):
    def __init__(self,attack=1,health=5,level=1,item=None,name="Peacock"):
        self.name = name
        self.attack = attack
        self.health = health
        self.abilityUses = self.level
    def copy(self):
        return Peacock(self.attack, self.health, self.level, self.item, self.name)
    def takeDamage(self,damage):
        if(damage > 0 and self.abilityUses > 0):
            self.attack += int((self.attack+1)/2)
            self.abilityUses -= 1
        self.health -= damage

class Shrimp(Pet):
    def __init__(self,attack=2,health=3,level=1,item=None,name="Shrimp"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Shrimp(self.attack, self.health, self.level, self.item, self.name)

class Swan(Pet):
    def __init__(self,attack=1,health=3,level=1,item=None,name="Swan"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Swan(self.attack, self.health, self.level, self.item, self.name)

class DirtyRat(Pet):
    def __init__(self,attack=1,health=1,level=1,item=None,name="DirtyRat"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return DirtyRat(self.attack, self.health, self.level, self.item, self.name)


## Tier Three Pets ##
## Missing Badger, Blowfish, Camel, Kangaroo, Ox, Turtle
class Dog(Pet):
    def __init__(self,attack=2,health=2,level=1,item=None,name="Dog"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Dog(self.attack, self.health, self.level, self.item, self.name)
    def petSpawned(self):
        if(random.randint(0,1) == 0):
            self.attack += 1*self.level
        else:
            self.health += 1*self.level
        return [0,0]

class Giraffe(Pet):
    def __init__(self,attack=2,health=5,level=1,item=None,name="Giraffe"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Giraffe(self.attack, self.health, self.level, self.item, self.name)

class Rabbit(Pet):
    def __init__(self,attack=3,health=2,level=1,item=None,name="Rabbit"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Rabbit(self.attack, self.health, self.level, self.item, self.name)

class Sheep(Pet):
    def __init__(self,attack=2,health=2,level=1,item=None,name="Sheep"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Sheep(self.attack, self.health, self.level, self.item, self.name)
    def faintSpawn(self):
        return [Ram(2*self.level), Ram(2*self.level)]

class Snail(Pet):
    def __init__(self,attack=2,health=2,level=1,item=None,name="Snail"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Snail(self.attack, self.health, self.level, self.item, self.name)

class Ram(Pet):
    def __init__(self,attack=2,health=2,level=1,item=None,name="Ram"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Ram(self.attack, self.health, self.level, self.item, self.name)


## Tier Four Pets ##
## Missing Whale, Hippo, Skunk,
class Bison(Pet):
    def __init__(self,attack=6,health=6,level=1,item=None,name="Bison"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Bison(self.attack, self.health, self.level, self.item, self.name)

class Deer(Pet):
    def __init__(self,attack=1,health=1,level=1,item=None,name="Deer"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Deer(self.attack, self.health, self.level, self.item, self.name)
    def faintSpawn(self):
        return [Bus(5*self.level,5*self.level,self.level)]

class Dolphin(Pet):
    def __init__(self,attack=4,health=6,level=1,item=None,name="Dolphin"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Dolphin(self.attack, self.health, self.level, self.item, self.name)
    def startBattleDamage(self, lenOtherParty,lowHealthIndex):
        damage = arrZeros(lenOtherParty)
        damage[lowHealthIndex] = 5*self.level
        return damage

class Penguin(Pet):
    def __init__(self,attack=1,health=2,level=1,item=None,name="Penguin"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Penguin(self.attack, self.health, self.level, self.item, self.name)

class Rooster(Pet):
    def __init__(self,attack=5,health=3,level=1,item=None,name="Rooster"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Rooster(self.attack, self.health, self.level, self.item, self.name)
    def faintSpawn(self):
        chickAttack = int(self.attack/2)
        chickArr = []
        for i in range(0,self.level):
            chickArr.append(Chick(chickAttack,1,self.level))
        return chickArr

class Squirrel(Pet):
    def __init__(self,attack=2,health=2,level=1,item=None,name="Squirrel"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Squirrel(self.attack, self.health, self.level, self.item, self.name)

class Worm(Pet):
    def __init__(self,attack=2,health=2,level=1,item=None,name="Worm"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Worm(self.attack, self.health, self.level, self.item, self.name)

class Bus(Pet):
    def __init__(self,attack=5,health=5,level=1,item=None,name="Bus"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Bus(self.attack, self.health, self.level, self.item, self.name)

class Chick(Pet):
    def __init__(self,attack=3,health=1,level=1,item=None,name="Chick"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Chick(self.attack, self.health, self.level, self.item, self.name)

## Tier Five Pets ##
## Missing Rhino
class Monkey(Pet):
    def __init__(self,attack=1,health=2,level=1,item=None,name="Monkey"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Monkey(self.attack, self.health, self.level, self.item, self.name)

class Cow(Pet):
    def __init__(self,attack=4,health=6,level=1,item=None,name="Cow"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Cow(self.attack, self.health, self.level, self.item, self.name)

class Crocodile(Pet):
    def __init__(self,attack=8,health=4,level=1,item=None,name="Crocodile"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Crocodile(self.attack, self.health, self.level, self.item, self.name)
    def startBattleDamage(self, lenOtherParty, lowHealthIndex):
        damage = arrZeros(lenOtherParty)
        damage[lenOtherParty-1] = 8*self.level
        print(damage)
        return damage

class Scorpion(Pet):
    def __init__(self,attack=1,health=1,level=1,item=None,name="Scorpion"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Scorpion(self.attack, self.health, self.level, self.item, self.name)

class Seal(Pet):
    def __init__(self,attack=3,health=8,level=1,item=None,name="Seal"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Seal(self.attack, self.health, self.level, self.item, self.name)

class Shark(Pet):
    def __init__(self,attack=4,health=4,level=1,item=None,name="Shark"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Shark(self.attack, self.health, self.level, self.item, self.name)
    def boostFromFaint(self, additions):
        self.attack += additions[0] + 2*self.level
        self.health += additions[1] + self.level

class Turkey(Pet):
    def __init__(self,attack=3,health=4,level=1,item=None,name="Turkey"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Turkey(self.attack, self.health, self.level, self.item, self.name)
    def petSpawned(self):
        return [3*self.level,3*self.level]


## Tier Six Pets ##
## Missing Boar, Fly, Gorilla, Snake, Tiger
class Cat(Pet):
    def __init__(self,attack=4,health=5,level=1,item=None,name="Cat"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Cat(self.attack, self.health, self.level, self.item, self.name)

class Dragon(Pet):
    def __init__(self,attack=6,health=8,level=1,item=None,name="Dragon"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Dragon(self.attack, self.health, self.level, self.item, self.name)

class Leopard(Pet):
    def __init__(self,attack=10,health=4,level=1,item=None,name="Leopard"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Leopard(self.attack, self.health, self.level, self.item, self.name)
    def startBattleDamage(self, lenOtherParty, lowHealthIndex):
        damage = arrZeros(lenOtherParty)
        selections = random.sample(range(0, lenOtherParty), min(self.level, lenOtherParty))
        for i in selections:
            damage[i] = int((self.attack+1)/2)
        return damage

class Mammoth(Pet):
    def __init__(self,attack=3,health=10,level=1,item=None,name="Mammoth"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return Mammoth(self.attack, self.health, self.level, self.item, self.name)
    def faintBoost(self,length):
        boosts = arrZeros(length,[2*self.level,2*self.level])
        return boosts

class ZFly(Pet):
    def __init__(self,attack=5,health=5,level=1,item=None,name="ZFly"):
        super().__init__(attack,health,level,item,name)
    def copy(self):
        return ZFly(self.attack, self.health, self.level, self.item, self.name)