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

    def startBattle(self):
        myDamage = self.myParty.startBattle(self.otherParty.len())
        otherDamage = self.otherParty.startBattle(self.myParty.len())
        print("Start Battle:", otherDamage, "   ", myDamage)
        self.myParty.takeDamage(otherDamage)
        self.otherParty.takeDamage(myDamage)

    def singleAttack(self):
        myDamage = self.myParty.getTurnDamage(self.otherParty.len())
        otherDamage = self.otherParty.getTurnDamage(self.myParty.len())
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