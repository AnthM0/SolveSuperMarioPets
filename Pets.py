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

print("...Pets Successfully Imported...")