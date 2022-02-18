import random

class Pet:
    def __init__(self,name,attack,health):
        self.name = name
        self.attack = attack
        self.health = health
    def copy(self):
        return Pet(self.name, self.attack, self.health)
    def addToParty(self,party):
        self.party = party
    def takeDamage(self,damage):
        self.health -= damage
    def getAttack(self,lenOtherParty,position):
        damageArr = arrZeros(lenOtherParty)
        if(position == 0):
            damageArr[0] += self.attack
        return damageArr
    def startBattle(self,lenOtherParty):
        self.attack = self.normAttack
        self.health = self.normHealth
        return arrZeros(lenOtherParty)
    def print(self):
        print(self.name,"(",self.attack,",",self.health,")   ",sep="",end="")
    def faint(self):
        return ""

class Fish(Pet):
    def __init__(self):
        self.name = "Fish"
        self.attack = 2
        self.health = 3
    def copy(self):
        return Fish(self.name, self.attack, self.health)

class Mosquito(Pet):
    def __init__(self):
        self.name = "Mosquito"
        self.attack = 2
        self.health = 2
    def copy(self):
        return Mosquito(self.name, self.attack, self.health)
    def startBattle(self,lenOtherParty):
        damage = arrZeros(lenOtherParty)
        damage[random.randint(0,lenOtherParty-1)] = 1
        return damage

print("Pets Successfully Imported")