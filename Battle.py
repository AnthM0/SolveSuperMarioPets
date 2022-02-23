class Battle:
    def __init__(self, myParty, otherParty):
        self.myParty = myParty
        self.otherParty = otherParty

    def print_battle(self):
        self.myParty.printB()
        print(" vs.   ", end="")
        self.otherParty.printF()
        print()

    def outcome(self):
        if self.myParty.is_alive() and self.otherParty.is_alive():
            return 69
        elif self.myParty.is_alive():
            return 1
        elif self.otherParty.is_alive():
            return -1
        return 0

    def start_battle(self, printing=False):
        if printing:
            self.print_battle()
        shots_fired = False
        shots_fired = self.myParty.start_battle(self.otherParty)
        shots_fired = self.otherParty.start_battle(self.myParty) or shots_fired
        while shots_fired:
            shots_fired = self.myParty.faint_scan(self.otherParty)
            shots_fired = self.otherParty.faint_scan(self.myParty) or shots_fired
        if printing:
            self.print_battle()
        return self.outcome()

    def turn(self, printing=False):
        self.before_attack(printing)

    def before_attack(self, printing=False):
        if printing:
            self.print_battle()
        shots_fired = False
        shots_fired = self.myParty.before_attack(self.otherParty)
        shots_fired = self.otherParty.before_attack(self.myParty) or shots_fired
        while shots_fired:
            shots_fired = self.myParty.faint_scan(self.otherParty)
            shots_fired = self.otherParty.faint_scan(self.myParty) or shots_fired
        if printing:
            self.print_battle()
        return self.outcome()

    def make_attack(self, printing=False):
        if printing:
            self.print_battle()
        shots_fired = True
        self.myParty.make_attack(self.otherParty)
        self.otherParty.make_attack(self.myParty)
        while shots_fired:
            shots_fired = self.myParty.faint_scan(self.otherParty)
            shots_fired = self.otherParty.faint_scan(self.myParty) or shots_fired
        if printing:
            self.print_battle()
        return self.outcome()

    def after_attack(self, printing=False):
        if printing:
            self.print_battle()
        shots_fired = False
        shots_fired = self.myParty.after_attack(self.otherParty)
        shots_fired = self.otherParty.after_attack(self.myParty) or shots_fired
        while shots_fired:
            shots_fired = self.myParty.faint_scan(self.otherParty)
            shots_fired = self.otherParty.faint_scan(self.myParty) or shots_fired
        if printing:
            self.print_battle()
        return self.outcome()
