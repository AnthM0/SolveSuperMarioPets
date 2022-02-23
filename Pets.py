import random
from SolveSuperMarioPets.Items import *


class Pet:
    def __init__(self, attack, health, level, item, name, hurt=False):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
        self.item = item
        self.hurt = hurt
    def copy(self, base=False):
        if base:
            return Pet()
        new_item = self.item.copy()
        return Pet(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def hash_string(self):
        ret_str = self.name + "[" + str(self.attack) + "," + str(self.health) + "," + str(self.level) + "]"
        ret_str = ret_str + self.item.hash_string()
        return ret_str
    def print(self):
        print(self.name, "(", self.attack, ",", self.health, ")   ", sep="", end="")

    def boost(self, additions):
        self.attack += additions[0]
        self.health += additions[1]
    def take_damage(self, damage, party, other_party):
        self.health -= damage
        self.hurt = True
    def was_hurt(self, party, other_party):
        self.hurt = False
        return False

    def start_battle(self, party, other_party):
        return False
    def before_attack(self, party, other_party):
        return False
    def make_attack(self, my_party, other_party):
        self.item.attack(self.attack, my_party, other_party)
    def after_attack(self, location, party, other_party):
        return False
    def faint(self, location, party, other_party):
        newPets = self.item.faint(self.copy(1), location, party)
        return False
    def friend_has_fainted(self, number, prev_party, n_party):
        return False
    def foe_has_fainted(self, old_foe_party, new_foe_party, party):
        return False
    def new_pet_spawning(self, new_pet):
        return False


# Tier One Pets #
class Ant(Pet):
    def __init__(self, attack=2, health=1, level=1, item=Item(), name="Ant", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Ant()
        new_item = self.item.copy()
        return Ant(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        if party.len() > 0:
            party.partyPets[random.randint(0, party.len()-1)].boost([2*self.level, self.level])
        super().faint(location, party, other_party)
        return False


class Beaver(Pet):
    def __init__(self, attack=2, health=2, level=1, item=Item(), name="Beaver", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Beaver()
        new_item = self.item.copy()
        return Beaver(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Cricket(Pet):
    def __init__(self, attack=1, health=2, level=1, item=Item(), name="Cricket", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Cricket()
        new_item = self.item.copy()
        return Cricket(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        spawns = [ZCricket(self.level, self.level, self.level)]
        party.spawn(spawns, location)
        super().faint(location, party, other_party)
        return False


class Duck(Pet):
    def __init__(self, attack=1, health=3, level=1, item=Item(), name="Duck", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Duck()
        new_item = self.item.copy()
        return Duck(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Fish(Pet):
    def __init__(self, attack=2, health=3, level=1, item=Item(), name="Fish", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Fish()
        new_item = self.item.copy()
        return Fish(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Horse(Pet):
    def __init__(self, attack=2, health=1, level=1, item=Item(), name="Horse", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Horse()
        new_item = self.item.copy()
        return Horse(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def new_pet_spawning(self, new_pet):
        new_pet.boost([self.level, 0])


class Mosquito(Pet):
    def __init__(self, attack=2, health=2, level=1, item=Item(), name="Mosquito", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Mosquito()
        new_item = self.item.copy()
        return Mosquito(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        attacks = self.level
        while attacks > 0:
            selections = random.sample(range(0, other_party.len()), min(attacks, other_party.len()))
            for i in selections:
                other_party.partyPets[i].take_damage(1, other_party, party)
                attacks -= 1
        return True


class Otter(Pet):
    def __init__(self, attack=1, health=2, level=1, item=Item(), name="Otter", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Otter()
        new_item = self.item.copy()
        return Otter(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Pig(Pet):
    def __init__(self, attack=3, health=1, level=1, item=Item(), name="Pig", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Pig()
        new_item = self.item.copy()
        return Pig(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class ZCricket(Pet):
    def __init__(self, attack=1, health=1, level=1, item=Item(), name="ZCricket", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return ZCricket()
        new_item = self.item.copy()
        return ZCricket(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Bee(Pet):
    def __init__(self, attack=1, health=1, level=1, item=Item(), name="Bee", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Bee()
        new_item = self.item.copy()
        return Bee(self.attack, self.health, self.level, new_item, self.name, self.hurt)


# Tier Two Pets #
class Crab(Pet):
    def __init__(self, attack=3, health=3, level=1, item=Item(), name="Crab", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Crab()
        new_item = self.item.copy()
        return Crab(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Dodo(Pet):
    def __init__(self, attack=2, health=3, level=1, item=Item(), name="Dodo", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Dodo()
        new_item = self.item.copy()
        return Dodo(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        if party.position(self) != 0:
            party.partyPets[party.position(self) - 1].boost([int((self.attack+1)/2*self.level), 0])
        return False


class Elephant(Pet):
    def __init__(self, attack=3, health=5, level=1, item=Item(), name="Elephant", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Elephant()
        new_item = self.item.copy()
        return Elephant(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def before_attack(self, party, other_party):
        if party.position(self) == 0 and party.len() > 1:
            party.partyPets[1].take_damage(1, party, other_party)
            if party.len() > 2 and self.level > 1:
                party.partyPets[2].take_damage(1, party, other_party)
                if party.len() > 3 and self.level > 2:
                    party.partyPets[3].take_damage(1, party, other_party)
            return True
        return False


class Flamingo(Pet):
    def __init__(self, attack=3, health=1, level=1, item=Item(), name="Flamingo", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Flamingo()
        new_item = self.item.copy()
        return Flamingo(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        if location < party.len():
            party.partyPets[location].boost([self.level, self.level])
        if (location+1) < party.len():
            party.partyPets[location+1].boost([self.level, self.level])
        super().faint(location, party, other_party)
        return False


class Hedgehog(Pet):
    def __init__(self, attack=3, health=2, level=1, item=Item(), name="Hedgehog", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Hedgehog()
        new_item = self.item.copy()
        return Hedgehog(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        for pet in party:
            pet.take_damage(2, party, other_party)
        for pet in other_party:
            pet.take_damage(2, other_party, party)
        super().faint(location, party, other_party)
        return True


class Peacock(Pet):
    def __init__(self, attack=1, health=5, level=1, item=Item(), name="Peacock", hurt=False):
        self.abilityUses = self.level
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Peacock()
        new_item = self.item.copy()
        return Peacock(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def was_hurt(self, party, other_party):
        if self.abilityUses > 0:
            self.attack += int((self.attack+1)/2)
            self.abilityUses -= 1
        return super().was_hurt(party, other_party)


class Rat(Pet):
    def __init__(self, attack=4, health=5, level=1, item=Item(), name="Rat", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Rat()
        new_item = self.item.copy()
        return Rat(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        spawns = []
        for i in range(0, self.level):
            spawns.append(DirtyRat(1, 1, self.level))
        other_party.spawn(spawns, 0)
        super().faint(location, party, other_party)
        return False


class Shrimp(Pet):
    def __init__(self, attack=2, health=3, level=1, item=Item(), name="Shrimp", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Shrimp()
        new_item = self.item.copy()
        return Shrimp(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Spider(Pet):
    def __init__(self, attack=2, health=2, level=1, item=Item(), name="Spider", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Spider()
        new_item = self.item.copy()
        return Spider(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        pets = [Dog(2, 2, self.level),
                Badger(2, 2, self.level),
                Blowfish(2, 2, self.level),
                Camel(2, 2, self.level),
                Giraffe(2, 2, self.level),
                Kangaroo(2, 2, self.level),
                Ox(2, 2, self.level),
                Rabbit(2, 2, self.level),
                Sheep(2, 2, self.level),
                Snail(2, 2, self.level),
                Turtle(2, 2, self.level)]
        spawns = [pets[random.randint(0, len(pets))]]
        party.spawn(spawns, location)
        super().faint(location, party, other_party)


class Swan(Pet):
    def __init__(self, attack=1, health=3, level=1, item=Item(), name="Swan", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Swan()
        new_item = self.item.copy()
        return Swan(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class DirtyRat(Pet):
    def __init__(self, attack=1, health=1, level=1, item=Item(), name="DirtyRat", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return DirtyRat()
        new_item = self.item.copy()
        return DirtyRat(self.attack, self.health, self.level, new_item, self.name, self.hurt)


# Tier Three Pets #
class Dog(Pet):
    def __init__(self, attack=2, health=2, level=1, item=Item(), name="Dog", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Dog()
        new_item = self.item.copy()
        return Dog(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def new_pet_spawning(self, new_pet):
        if random.randint(0, 1) == 0:
            self.attack += self.level
        else:
            self.health += self.level


class Badger(Pet):
    def __init__(self, attack=5, health=4, level=1, item=Item(), name="Badger", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Badger()
        new_item = self.item.copy()
        return Badger(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        damage = self.attack*self.level
        if location == 0:
            other_party.partyPets[0].take_damage(damage, other_party, party)
        if location < party.len():
            party.partyPets[location].take_damage(damage, party, other_party)
        super().faint(location, party, other_party)
        return True


class Blowfish(Pet):
    def __init__(self, attack=3, health=5, level=1, item=Item(), name="Blowfish", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Blowfish()
        new_item = self.item.copy()
        return Blowfish(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def was_hurt(self, party, other_party):
        if self.hurt:
            other_party.partyPets[random.randint(0, other_party.len()-1)].take_damage(2*self.level, other_party, party)
            self.hurt = False
            return True
        return super().was_hurt(party, other_party)


class Camel(Pet):
    def __init__(self, attack=2, health=5, level=1, item=Item(), name="Camel", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Camel()
        new_item = self.item.copy()
        return Camel(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def was_hurt(self, party, other_party):
        if party.len() > (party.position(self)+1):
            party.partyPets[(party.position(self)+1)].boost([self.level, 2*self.level])
        return super().was_hurt(party, other_party)


class Giraffe(Pet):
    def __init__(self, attack=2, health=5, level=1, item=Item(), name="Giraffe", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Giraffe()
        new_item = self.item.copy()
        return Giraffe(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Kangaroo(Pet):
    def __init__(self, attack=1, health=2, level=1, item=Item(), name="Kangaroo", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Kangaroo()
        new_item = self.item.copy()
        return Kangaroo(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def after_attack(self, location, party, other_party):
        if location == 1:
            self.boost([2*self.level, 2*self.level])
        return False


class Ox(Pet):
    def __init__(self, attack=1, health=4, level=1, item=Item(), name="Ox", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Ox()
        new_item = self.item.copy()
        return Ox(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def friend_has_fainted(self, number, prev_party, n_party):
        old_position = prev_party.position(self)
        new_position = n_party.position(self)
        if old_position > 0:
            if new_position == 0:
                self.boost([2*self.level, 0])
                self.item = Melon()
            elif prev_party.partyPets[old_position-1] != n_party.partyPets[new_position-1]:
                self.boost([2 * self.level, 0])
                self.item = Melon()


class Rabbit(Pet):
    def __init__(self, attack=3, health=2, level=1, item=Item(), name="Rabbit", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Rabbit()
        new_item = self.item.copy()
        return Rabbit(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Sheep(Pet):
    def __init__(self, attack=2, health=2, level=1, item=Item(), name="Sheep", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Sheep()
        new_item = self.item.copy()
        return Sheep(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        spawns = [Ram(2*self.level, 2*self.level, self.level), Ram(2*self.level, 2*self.level, self.level)]
        party.spawn(spawns, location)
        super().faint(location, party, other_party)
        return False


class Snail(Pet):
    def __init__(self, attack=2, health=2, level=1, item=Item(), name="Snail", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Snail()
        new_item = self.item.copy()
        return Snail(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Turtle(Pet):
    def __init__(self, attack=2, health=2, level=1, item=Item(), name="Turtle", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Turtle()
        new_item = self.item.copy()
        return Turtle(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        if party.position(self) == 0 and party.len() > 1:
            party.partyPets[1].item = Melon()
            if party.len() > 2 and self.level > 1:
                party.partyPets[2].item = Melon()
                if party.len() > 3 and self.level > 2:
                    party.partyPets[3].item = Melon()
        super().faint(location, party, other_party)
        return False


class Ram(Pet):
    def __init__(self, attack=2, health=2, level=1, item=Item(), name="Ram", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Ram()
        new_item = self.item.copy()
        return Ram(self.attack, self.health, self.level, new_item, self.name, self.hurt)


# Tier Four Pets #
class Whale(Pet):
    def __init__(self, attack=3, health=8, level=1, item=Item(), name="Whale", stored_pet=None, hurt=False):
        self.stored_pet = stored_pet
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Whale()
        new_item = self.item.copy()
        return Whale(self.attack, self.health, self.level, self.item, self.name, self.stored_pet, self.hurt)
    def faint(self, location, party, other_party):
        party.spawn([self.stored_pet], location)
        super().faint(location, party, other_party)
        return False
    def start_battle(self, party, other_party):
        if party.position(self) != 0:
            target_pet = party.partyPets[party.position(self)-1]
            self.stored_pet = target_pet.copy(True)
            self.stored_pet.level = self.level
            target_pet.health = 0
        return True


class Bison(Pet):
    def __init__(self, attack=6, health=6, level=1, item=Item(), name="Bison", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Bison()
        new_item = self.item.copy()
        return Bison(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Deer(Pet):
    def __init__(self, attack=1, health=1, level=1, item=Item(), name="Deer", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Deer()
        new_item = self.item.copy()
        return Deer(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        spawns = [Bus(5*self.level, 5*self.level, self.level)]
        party.spawn(spawns, location)
        super().faint(location, party, other_party)
        return False


class Dolphin(Pet):
    def __init__(self, attack=4, health=6, level=1, item=Item(), name="Dolphin", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Dolphin()
        new_item = self.item.copy()
        return Dolphin(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        other_party.low_health_pet().take_damage(5*self.level, other_party, party)
        return True


class Hippo(Pet):
    def __init__(self, attack=4, health=7, level=1, item=Item(), name="Hippo", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Hippo()
        new_item = self.item.copy()
        return Hippo(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def foe_has_fainted(self, location, party, other_party):
        if location == 0:
            self.boost([2*self.level, 2*self.level])
        return False


class Penguin(Pet):
    def __init__(self, attack=1, health=2, level=1, item=Item(), name="Penguin", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Penguin()
        new_item = self.item.copy()
        return Penguin(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Rooster(Pet):
    def __init__(self, attack=5, health=3, level=1, item=Item(), name="Rooster", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Rooster()
        new_item = self.item.copy()
        return Rooster(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        chick_attack = int((self.attack+1)/2)
        spawns = []
        for i in range(0, self.level):
            spawns.append(Chick(chick_attack, 1, self.level))
        party.spawn(spawns, location)
        super().faint(location, party, other_party)
        return False


class Skunk(Pet):
    def __init__(self, attack=3, health=6, level=1, item=Item(), name="Skunk", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Skunk()
        new_item = self.item.copy()
        return Skunk(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        high_health_pet = other_party.high_health_pet()
        high_health_pet.health = int((high_health_pet.health*(3-self.level)/3)+1)
        return False


class Squirrel(Pet):
    def __init__(self, attack=2, health=2, level=1, item=Item(), name="Squirrel", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Squirrel()
        new_item = self.item.copy()
        return Squirrel(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Worm(Pet):
    def __init__(self, attack=2, health=2, level=1, item=Item(), name="Worm", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Worm()
        new_item = self.item.copy()
        return Worm(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Bus(Pet):
    def __init__(self, attack=5, health=5, level=1, item=Chili(), name="Bus", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Bus()
        new_item = self.item.copy()
        return Bus(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Chick(Pet):
    def __init__(self, attack=3, health=1, level=1, item=Item(), name="Chick", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Chick()
        new_item = self.item.copy()
        return Chick(self.attack, self.health, self.level, new_item, self.name, self.hurt)


# Tier Five Pets #
class Monkey(Pet):
    def __init__(self, attack=1, health=2, level=1, item=Item(), name="Monkey", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Monkey()
        new_item = self.item.copy()
        return Monkey(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Cow(Pet):
    def __init__(self, attack=4, health=6, level=1, item=Item(), name="Cow", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Cow()
        new_item = self.item.copy()
        return Cow(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Crocodile(Pet):
    def __init__(self, attack=8, health=4, level=1, item=Item(), name="Crocodile", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Crocodile()
        new_item = self.item.copy()
        return Crocodile(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        other_party.partyPets[-1].take_damage(8*self.level, other_party, party)
        return True


class Rhino(Pet):
    def __init__(self, attack=4, health=7, level=1, item=Item(), name="Rhino", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Rhino()
        new_item = self.item.copy()
        return Rhino(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def foe_has_fainted(self, location, party, other_party):
        if location == 0:
            if other_party.len() > 0:
                other_party.partyPets[0].take_damage(5*self.level, other_party, party)
        return True


class Scorpion(Pet):
    def __init__(self, attack=1, health=1, level=1, item=Peanut(), name="Scorpion", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Scorpion()
        new_item = self.item.copy()
        return Scorpion(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Seal(Pet):
    def __init__(self, attack=3, health=8, level=1, item=Item(), name="Seal", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Seal()
        new_item = self.item.copy()
        return Seal(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Shark(Pet):
    def __init__(self, attack=4, health=4, level=1, item=Item(), name="Shark", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Shark()
        new_item = self.item.copy()
        return Shark(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def friend_has_fainted(self, number, prev_party, n_party):
        self.boost([2*self.level*number, self.level*number])


class Turkey(Pet):
    def __init__(self, attack=3, health=4, level=1, item=Item(), name="Turkey", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Turkey()
        new_item = self.item.copy()
        return Turkey(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def new_pet_spawning(self, new_pet):
        new_pet.boost([3*self.level, 3*self.level])


# Tier Six Pets #
class Cat(Pet):
    def __init__(self, attack=4, health=5, level=1, item=Item(), name="Cat", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Cat()
        new_item = self.item.copy()
        return Cat(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Boar(Pet):
    def __init__(self, attack=8, health=6, level=1, item=Item(), name="Boar", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Boar()
        new_item = self.item.copy()
        return Boar(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def before_attack(self, party, other_party):
        self.boost([2*self.level, 2*self.level])
        return False


class Dragon(Pet):
    def __init__(self, attack=6, health=8, level=1, item=Item(), name="Dragon", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Dragon()
        new_item = self.item.copy()
        return Dragon(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class Fly(Pet):
    def __init__(self, attack=5, health=5, level=1, item=Item(), name="Fly", hurt=False):
        self.abilityUses = 3
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Fly()
        new_item = self.item.copy()
        return Fly(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def friend_has_fainted(self, number, prev_party, n_party):
        if self.abilityUses > 0:
            if n_party.spawn(ZFly(5*self.level, 5*self.level, self.level)):
                self.abilityUses -= 1


class Gorilla(Pet):
    def __init__(self, attack=6, health=9, level=1, item=Item(), name="Gorilla", hurt=False):
        self.abilityUses = self.level
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Gorilla()
        new_item = self.item.copy()
        return Gorilla(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def was_hurt(self, party, other_party):
        if self.abilityUses > 0:
            self.abilityUses -= 1
            self.item = Coconut()
        return super().was_hurt(party, other_party)


class Leopard(Pet):
    def __init__(self, attack=10, health=4, level=1, item=Item(), name="Leopard", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Leopard()
        new_item = self.item.copy()
        return Leopard(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        attacks = self.level
        while attacks > 0:
            selections = random.sample(range(0, other_party.len()), min(attacks, other_party.len()))
            for i in selections:
                other_party.partyPets[i].take_damage(int((self.attack+1)/2), other_party, party)
                attacks -= 1
        return True


class Mammoth(Pet):
    def __init__(self, attack=3, health=10, level=1, item=Item(), name="Mammoth", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Mammoth()
        new_item = self.item.copy()
        return Mammoth(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        for pet in party.partyPets:
            pet.boost([2*self.level, 2*self.level])
        super().faint(location, party, other_party)
        return False


class Snake(Pet):
    def __init__(self, attack=6, health=6, level=1, item=Item(), name="Snake", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Snake()
        new_item = self.item.copy()
        return Snake(self.attack, self.health, self.level, new_item, self.name, self.hurt)
    def after_attack(self, location, party, other_party):
        if location == 1:
            other_party.partyPets[random.randint(0, other_party.len() - 1)].take_damage(5*self.level, party, other_party)
            return True
        return False


class Tiger(Pet):
    def __init__(self, attack=4, health=3, level=1, item=Item(), name="Tiger", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return Tiger()
        new_item = self.item.copy()
        return Tiger(self.attack, self.health, self.level, new_item, self.name, self.hurt)


class ZFly(Pet):
    def __init__(self, attack=5, health=5, level=1, item=Item(), name="ZFly", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self, base=False):
        if base:
            return ZFly()
        new_item = self.item.copy()
        return ZFly(self.attack, self.health, self.level, new_item, self.name, self.hurt)
