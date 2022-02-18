import random
from OtherFunctions import *

class Pet:
    def __init__(self,name,attack,health):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Pet(self.name, self.attack, self.health)
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
    def faint(self):
        return []
    def petSpawned(self):
        return [0,0]

class Ant(Pet):
    def __init__(self,name="Fish",attack=2,health=1):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Fish(self.name, self.attack, self.health)

class Beaver(Pet):
    def __init__(self,name="Beaver",attack=2,health=2):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Beaver(self.name, self.attack, self.health)

class Cricket(Pet):
    def __init__(self,name="Cricket",attack=1,health=2):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Cricket(self.name, self.attack, self.health)
    def faint(self):
        return [ZCricket()]

class Duck(Pet):
    def __init__(self,name="Duck",attack=1,health=3):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Duck(self.name, self.attack, self.health)

class Fish(Pet):
    def __init__(self,name="Fish",attack=2,health=3):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Fish(self.name, self.attack, self.health)

class Horse(Pet):
    def __init__(self,name="Horse",attack=2,health=1):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Horse(self.name, self.attack, self.health)
    def petSpawned(self):
        return [1,0]

class Mosquito(Pet):
    def __init__(self,name="Mosquito",attack=2,health=2):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Mosquito(self.name, self.attack, self.health)
    def startBattle(self,lenOtherParty):
        damage = arrZeros(lenOtherParty)
        damage[random.randint(0,lenOtherParty-1)] = 1
        return damage

class Otter(Pet):
    def __init__(self,name="Otter",attack=1,health=2):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Otter(self.name, self.attack, self.health)

class Pig(Pet):
    def __init__(self,name="Pig",attack=3,health=1):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Pig(self.name, self.attack, self.health)

class ZCricket(Pet):
    def __init__(self,name="ZCricket",attack=1,health=1):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return ZCricket(self.name, self.attack, self.health)

print("...Pets Successfully Imported...")