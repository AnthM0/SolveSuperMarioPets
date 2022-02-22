import random


class Pet:
    def __init__(self, attack, health, level, item, name, hurt=False):
        self.name = name
        self.attack = attack
        self.health = health
        self.level = level
        self.item = item
        self.hurt = hurt
    def copy(self):
        return Pet(self.attack, self.health, self.level, self.item, self.name, self.hurt)
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
        other_party.partyPets[0].take_damage(self.attack, my_party, other_party)
    def after_attack(self, location, party, other_party):
        return False
    def faint(self, location, party, other_party):
        return False
    def friend_has_fainted(self, number, prev_party, n_party):
        return False
    def foe_has_fainted(self, old_foe_party, new_foe_party, party):
        return False
    def new_pet_spawning(self, new_pet):
        return False


# Tier One Pets #
class Ant(Pet):
    def __init__(self, attack=2, health=1, level=1, item=None, name="Ant", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Ant(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        party.partyPets[random.randint(0, party.len()-1)].boost([2*self.level, self.level])


class Beaver(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Beaver", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Beaver(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Cricket(Pet):
    def __init__(self, attack=1, health=2, level=1, item=None, name="Cricket", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Cricket(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        spawns = [ZCricket(self.level, self.level, self.level)]
        party.spawn(spawns, location)


class Duck(Pet):
    def __init__(self, attack=1, health=3, level=1, item=None, name="Duck", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Duck(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Fish(Pet):
    def __init__(self, attack=2, health=3, level=1, item=None, name="Fish", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Fish(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Horse(Pet):
    def __init__(self, attack=2, health=1, level=1, item=None, name="Horse", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Horse(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def new_pet_spawning(self, new_pet):
        new_pet.boost([self.level, 0])


class Mosquito(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Mosquito", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Mosquito(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        attacks = self.level
        while attacks > 0:
            selections = random.sample(range(0, other_party.len()), min(attacks, other_party.len()))
            for i in selections:
                other_party.partyPets[i].take_damage(1, other_party, party)
                attacks -= 1
        return True


class Otter(Pet):
    def __init__(self, attack=1, health=2, level=1, item=None, name="Otter", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Otter(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Pig(Pet):
    def __init__(self, attack=3, health=1, level=1, item=None, name="Pig", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Pig(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class ZCricket(Pet):
    def __init__(self, attack=1, health=1, level=1, item=None, name="ZCricket", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return ZCricket(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Bee(Pet):
    def __init__(self, attack=1, health=1, level=1, item=None, name="Bee", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Bee(self.attack, self.health, self.level, self.item, self.name, self.hurt)


# Tier Two Pets #
class Crab(Pet):
    def __init__(self, attack=3, health=3, level=1, item=None, name="Crab", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Crab(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Dodo(Pet):
    def __init__(self, attack=2, health=3, level=1, item=None, name="Dodo", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Dodo(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        if party.position(self) != 0:
            party.partyPets[party.position(self) - 1].boost([int((self.attack+1)/2*self.level), 0])
        return False


class Elephant(Pet):
    def __init__(self, attack=3, health=5, level=1, item=None, name="Elephant", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Elephant(self.attack, self.health, self.level, self.item, self.name, self.hurt)
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
    def __init__(self, attack=3, health=1, level=1, item=None, name="Flamingo", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Flamingo(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        if location < party.len():
            party.partyPets[location].boost([self.level, self.level])
        if (location+1) < party.len():
            party.partyPets[location+1].boost([self.level, self.level])
        return False


class Hedgehog(Pet):
    def __init__(self, attack=3, health=2, level=1, item=None, name="Hedgehog", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Hedgehog(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        for pet in party:
            pet.take_damage(2, party, other_party)
        for pet in other_party:
            pet.take_damage(2, other_party, party)
        return True


class Peacock(Pet):
    def __init__(self, attack=1, health=5, level=1, item=None, name="Peacock", hurt=False):
        self.abilityUses = self.level
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Peacock(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def was_hurt(self, party, other_party):
        if self.abilityUses > 0:
            self.attack += int((self.attack+1)/2)
            self.abilityUses -= 1
        return super().was_hurt(party, other_party)


class Rat(Pet):
    def __init__(self, attack=4, health=5, level=1, item=None, name="Rat", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Rat(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        spawns = []
        for i in range(0, self.level):
            spawns.append(DirtyRat(1, 1, self.level))
        other_party.spawn(spawns, 0)


class Shrimp(Pet):
    def __init__(self, attack=2, health=3, level=1, item=None, name="Shrimp", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Shrimp(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Spider(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Spider", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Spider(self.attack, self.health, self.level, self.item, self.name, self.hurt)
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
        spawns = [pets[random.randint(0,len(pets))]]
        party.spawn(spawns, location)


class Swan(Pet):
    def __init__(self, attack=1, health=3, level=1, item=None, name="Swan", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Swan(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class DirtyRat(Pet):
    def __init__(self, attack=1, health=1, level=1, item=None, name="DirtyRat", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return DirtyRat(self.attack, self.health, self.level, self.item, self.name, self.hurt)


# Tier Three Pets #
class Dog(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Dog", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Dog(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def new_pet_spawning(self, new_pet):
        if random.randint(0, 1) == 0:
            self.attack += self.level
        else:
            self.health += self.level


class Badger(Pet):
    def __init__(self, attack=5, health=4, level=1, item=None, name="Badger", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Badger(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        damage = self.attack*self.level
        if location == 0:
            other_party.partyPets[0].take_damage(damage, other_party, party)
        if location < party.len():
            party.partyPets[location].take_damage(damage, party, other_party)
        return True


class Blowfish(Pet):
    def __init__(self, attack=3, health=5, level=1, item=None, name="Blowfish", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Blowfish(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def was_hurt(self, party, other_party):
        if self.hurt:
            other_party.partyPets[random.randint(0, other_party.len()-1)].take_damage(2*self.level, other_party, party)
            self.hurt = False
            return True
        return super().was_hurt(party, other_party)


class Camel(Pet):
    def __init__(self, attack=2, health=5, level=1, item=None, name="Camel", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Camel(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def was_hurt(self, party, other_party):
        if party.len() > (party.position(self)+1):
            party.partyPets[(party.position(self)+1)].boost([self.level, 2*self.level])
        return super().was_hurt(party, other_party)


class Giraffe(Pet):
    def __init__(self, attack=2, health=5, level=1, item=None, name="Giraffe", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Giraffe(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Kangaroo(Pet):
    def __init__(self, attack=2, health=5, level=1, item=None, name="Kangaroo", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Kangaroo(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def after_attack(self, location, party, other_party):
        if location == 1:
            self.boost([2*self.level, 2*self.level])
        return False


class Ox(Pet):
    def __init__(self, attack=1, health=4, level=1, item=None, name="Ox", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Ox(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def friend_has_fainted(self, number, prev_party, n_party):
        old_position = prev_party.position(self)
        new_position = n_party.position(self)
        if old_position > 0:
            if new_position == 0:
                self.boost([2*self.level, 0])
            elif prev_party.partyPets[old_position-1] != n_party.partyPets[new_position-1]:
                self.boost([2 * self.level, 0])


class Rabbit(Pet):
    def __init__(self, attack=3, health=2, level=1, item=None, name="Rabbit", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Rabbit(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Sheep(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Sheep", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Sheep(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        spawns = [Ram(2*self.level, 2*self.level, self.level), Ram(2*self.level, 2*self.level, self.level)]
        party.spawn(spawns, location)


class Snail(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Snail", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Snail(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Turtle(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Turtle", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Turtle(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Ram(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Ram", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Ram(self.attack, self.health, self.level, self.item, self.name, self.hurt)


# Tier Four Pets #
class Whale(Pet):
    def __init__(self, attack=3, health=8, level=1, item=None, name="Whale", stored_pet=None, hurt=False):
        self.stored_pet = stored_pet
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Whale(self.attack, self.health, self.level, self.item, self.name, self.stored_pet, self.hurt)
    def faint(self, location, party, other_party):
        party.spawn([self.stored_pet], location)
    def start_battle(self, party, other_party):
        if party.position(self) != 0:
            target_pet = party.partyPets[party.position(self)-1]
            self.stored_pet = target_pet.copy()
            self.stored_pet.attack = 1
            self.stored_pet.health = 1
            target_pet.health = 0
        return True


class Bison(Pet):
    def __init__(self, attack=6, health=6, level=1, item=None, name="Bison", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Bison(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Deer(Pet):
    def __init__(self, attack=1, health=1, level=1, item=None, name="Deer", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Deer(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        spawns = [Bus(5*self.level, 5*self.level, self.level)]
        party.spawn(spawns, location)


class Dolphin(Pet):
    def __init__(self, attack=4, health=6, level=1, item=None, name="Dolphin", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Dolphin(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        other_party.low_health_pet().take_damage(5*self.level, other_party, party)
        return True


class Hippo(Pet):
    def __init__(self, attack=4, health=7, level=1, item=None, name="Hippo", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Hippo(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def foe_has_fainted(self, location, party, other_party):
        if location == 0:
            self.boost([2*self.level, 2*self.level])
        return False


class Penguin(Pet):
    def __init__(self, attack=1, health=2, level=1, item=None, name="Penguin", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Penguin(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Rooster(Pet):
    def __init__(self, attack=5, health=3, level=1, item=None, name="Rooster", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Rooster(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        chick_attack = int((self.attack+1)/2)
        spawns = []
        for i in range(0, self.level):
            spawns.append(Chick(chick_attack, 1, self.level))
        party.spawn(spawns, location)


class Skunk(Pet):
    def __init__(self, attack=3, health=6, level=1, item=None, name="Skunk", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Skunk(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        high_health_pet = other_party.high_health_pet()
        high_health_pet.health = int((high_health_pet.health*(3-self.level)/3)+1)
        return False


class Squirrel(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Squirrel", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Squirrel(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Worm(Pet):
    def __init__(self, attack=2, health=2, level=1, item=None, name="Worm", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Worm(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Bus(Pet):
    def __init__(self, attack=5, health=5, level=1, item=None, name="Bus", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Bus(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Chick(Pet):
    def __init__(self, attack=3, health=1, level=1, item=None, name="Chick", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Chick(self.attack, self.health, self.level, self.item, self.name, self.hurt)


# Tier Five Pets #
class Monkey(Pet):
    def __init__(self, attack=1, health=2, level=1, item=None, name="Monkey", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Monkey(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Cow(Pet):
    def __init__(self, attack=4, health=6, level=1, item=None, name="Cow", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Cow(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Crocodile(Pet):
    def __init__(self, attack=8, health=4, level=1, item=None, name="Crocodile", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Crocodile(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        other_party.partyPets[-1].take_damage(8*self.level, other_party, party)
        return True


class Rhino(Pet):
    def __init__(self, attack=4, health=7, level=1, item=None, name="Rhino", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Rhino(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def foe_has_fainted(self, location, party, other_party):
        if location == 0:
            if other_party.len() > 0:
                other_party.partyPets[0].take_damage(5*self.level, other_party, party)
        return True


class Scorpion(Pet):
    def __init__(self, attack=1, health=1, level=1, item=None, name="Scorpion", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Scorpion(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Seal(Pet):
    def __init__(self, attack=3, health=8, level=1, item=None, name="Seal", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Seal(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Shark(Pet):
    def __init__(self, attack=4, health=4, level=1, item=None, name="Shark", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Shark(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def friend_has_fainted(self, number, prev_party, n_party):
        self.boost([2*self.level*number, self.level*number])


class Turkey(Pet):
    def __init__(self, attack=3, health=4, level=1, item=None, name="Turkey", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Turkey(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def new_pet_spawning(self, new_pet):
        new_pet.boost([3*self.level, 3*self.level])


# Tier Six Pets #
class Cat(Pet):
    def __init__(self, attack=4, health=5, level=1, item=None, name="Cat", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Cat(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Boar(Pet):
    def __init__(self, attack=8, health=6, level=1, item=None, name="Boar", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Boar(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def before_attack(self, party, other_party):
        self.boost([2*self.level, 2*self.level])
        return False


class Dragon(Pet):
    def __init__(self, attack=6, health=8, level=1, item=None, name="Dragon", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Dragon(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class Fly(Pet):
    def __init__(self, attack=5, health=5, level=1, item=None, name="Fly", hurt=False):
        self.abilityUses = 3
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Fly(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def friend_has_fainted(self, number, prev_party, n_party):
        if self.abilityUses > 0:
            if n_party.spawn(ZFly(5*self.level, 5*self.level, self.level)):
                self.abilityUses -= 1


class Gorilla(Pet):
    def __init__(self, attack=6, health=9, level=1, item=None, name="Gorilla", hurt=False):
        self.abilityUses = self.level
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Gorilla(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def was_hurt(self, party, other_party):
        if self.abilityUses > 0:
            self.abilityUses -= 1
        return super().was_hurt(party, other_party)


class Leopard(Pet):
    def __init__(self, attack=10, health=4, level=1, item=None, name="Leopard", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Leopard(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def start_battle(self, party, other_party):
        attacks = self.level
        while attacks > 0:
            selections = random.sample(range(0, other_party.len()), min(attacks, other_party.len()))
            for i in selections:
                other_party.partyPets[i].take_damage(int((self.attack+1)/2), other_party, party)
                attacks -= 1
        return True


class Mammoth(Pet):
    def __init__(self, attack=3, health=10, level=1, item=None, name="Mammoth", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Mammoth(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def faint(self, location, party, other_party):
        for pet in party.partyPets:
            pet.boost([2*self.level, 2*self.level])


class Snake(Pet):
    def __init__(self, attack=6, health=6, level=1, item=None, name="Snake", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Snake(self.attack, self.health, self.level, self.item, self.name, self.hurt)
    def after_attack(self, location, party, other_party):
        if location == 1:
            other_party.partyPets[random.randint(0, other_party.len() - 1)].take_damage(5*self.level, party, other_party)
            return True
        return False


class Tiger(Pet):
    def __init__(self, attack=4, health=3, level=1, item=None, name="Tiger", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return Tiger(self.attack, self.health, self.level, self.item, self.name, self.hurt)


class ZFly(Pet):
    def __init__(self, attack=5, health=5, level=1, item=None, name="ZFly", hurt=False):
        super().__init__(attack, health, level, item, name, hurt)
    def copy(self):
        return ZFly(self.attack, self.health, self.level, self.item, self.name, self.hurt)
