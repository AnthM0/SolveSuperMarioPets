class Battle:
    def __init__(self,myParty,otherParty):
        self.myParty = myParty
        self.otherParty = otherParty

    def printBattle(self):
        lenMyParty = len(self.myParty.partyPets)
        for i in range(lenMyParty,5):
            print(" ", end="")
        self.myParty.printB()
        print("    ", end="")
        self.otherParty.printF()
        print()

    def startBattle(self,printing=False):
        myDamage = self.myParty.startBattleDamage(self.otherParty.len(), self.otherParty.lowHealthIndex())
        otherDamage = self.otherParty.startBattleDamage(self.myParty.len(), self.myParty.lowHealthIndex())
        if(printing):
            print("Start Battle:", otherDamage, "   ", myDamage)
        self.myParty.takeDamage(otherDamage)
        self.otherParty.takeDamage(myDamage)

    def singleAttack(self,printing=False):
        myDamage = self.myParty.getTurnDamage(self.otherParty.len())
        otherDamage = self.otherParty.getTurnDamage(self.myParty.len())
        if (printing):
            print("Attack: ", otherDamage, "   ", myDamage)
        self.myParty.takeDamage(otherDamage)
        self.otherParty.takeDamage(myDamage)

    def checkOutcome(self):
        if(self.myParty.isAlive() and self.otherParty.isAlive()):
            return 69
        elif(self.myParty.isAlive()):
            return 1
        elif(self.otherParty.isAlive()):
            return -1
        return 0