from SolveSuperMarioPets.Pets import *


class Item:
    def __init__(self, name="", used=False):
        self.name = name
        self.used = used
    def copy(self):
        return Item(self.name)
    def attack(self, base_attack, party, other_party):
        other_party.partyPets[0].take_damage(base_attack, other_party, party)
    def take_damage(self, damage):
        if damage < 0:
            return 0
        return damage
    def blocks_damage(self, damage):
        return False
    def faint(self, copy, location, party):
        return []


class MeatBone(Item):
    def __init__(self, name="MeatBone", used=False):
        super().__init__(name, used)
    def copy(self):
        return MeatBone(self.name)
    def attack(self, base_attack, party, other_party):
        super().attack(base_attack+5, party, other_party)


class Chili(Item):
    def __init__(self, name="Chili", used=False):
        super().__init__(name, used)
    def copy(self):
        return Chili(self.name)
    def attack(self, base_attack, party, other_party):
        if other_party.len() > 1:
            other_party.partyPets[1].take_damage(5, other_party, party)
        super().attack(base_attack, party, other_party)


class Steak(Item):
    def __init__(self, name="Steak", used=False):
        super().__init__(name, used)
    def copy(self):
        return Steak(self.name, self.used)
    def attack(self, base_attack, party, other_party):
        if self.used:
            super().attack(base_attack, party, other_party)
        else:
            self.used = True
            super().attack(base_attack+20, party, other_party)


class Peanut(Item):
    def __init__(self, name="Peanut", used=False):
        super().__init__(name, used)
    def copy(self):
        return Peanut(self.name)
    def attack(self, base_attack, party, other_party):
        if other_party.partyPets[0].item.blocks_damage(base_attack):
            super().attack(base_attack, party, other_party)
        else:
            other_party.partyPets[0].health = -100


class Melon(Item):
    def __init__(self, name="Melon", used=False):
        super().__init__(name, used)
    def copy(self):
        return Melon(self.name, self.used)
    def take_damage(self, damage):
        if self.used:
            return super().take_damage(damage)
        else:
            self.used = True
            return super().take_damage(damage-20)
    def blocks_damage(self, damage):
        if self.used or damage > 20:
            return False
        return True


class Coconut(Item):
    def __init__(self, name="Coconut", used=False):
        super().__init__(name, used)
    def copy(self):
        return Coconut(self.name, self.used)
    def take_damage(self, damage):
        if self.used:
            return super().take_damage(0)
        return super().take_damage(damage)
    def blocks_damage(self, damage):
        if self.used:
            return False
        return True


class Garlic(Item):
    def __init__(self, name="Garlic", used=False):
        super().__init__(name, used)
    def copy(self):
        return Garlic(self.name)
    def take_damage(self, damage):
        if damage < 3:
            return super().take_damage(1)
        else:
            return super().take_damage(damage-2)


class Honey(Item):
    def __init__(self, name="Honey", used=False):
        super().__init__(name, used)
    def copy(self):
        return Honey(self.name)
    def faint(self, copy, location, party):
        party.spawn([Bee()], location)


class Mushroom(Item):
    def __init__(self, name="Mushroom", used=False):
        super().__init__(name, used)
    def copy(self):
        return Mushroom(self.name)
    def faint(self, copy, location, party):
        copy.attack = 1
        copy.health = 1
        spawns = [copy]
        party.spawn(spawns, location)
