"""
exercise: Object oriented role playing game, part 2 :

As always, read the whole exercise description carefully before your start to solve the exercise.

Build on your solution of part 1.

Invent two new classes, which inherit from class Character. For example Hunter and Magician.
Your new classes shall have their own additional methods and/or attributes. Maybe they also override methods or attributes from class Character.

In the main program, let objects of your new classes fight against each other until one character is dead.
Print out what happens during the fight.

In each turn, a character uses one of its capabilities (methods). Then it's the other character's turn.
It is up to you, how your program decides in each turn, which capability to use.
For example, the decision may be based on randomness or on a clever strategy

Upgrade 1:
Each time a character uses one of it's capabilities, add some randomness to the used power.

Upgrade 2:
Let your characters fight against each other 100 times.
Keep track of the results.
Try to balance your character's capabilities in such a way that each character wins about half of the fights.

If you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""
import random

class Character:

    def __init__(self, name = "" , health = 100, attackpower = 10):
        self.Max_health = health
        self._current_health = self.Max_health
        self.attackpower = attackpower
        self.name = name

    def __repr__(self):
        return f"name:{self.name}. health:{self._current_health}. max health:{self.Max_health}. attackpower:{self.attackpower}."

    def hit(self, victem):
        victem.get_hit(self)

    def get_hit(self, attacker):
        self._current_health -= int(attacker.attackpower * self.rangecalc())

    def get_healed(self, healer):
        self._current_health += int(healer.healpower * self.rangecalc())

    def get_health(self):
        return self._current_health

    def rangecalc(self):
        return float(random.randint(75,125)) / float(100)

class Healer(Character):

    def __init__(self, name ="", health = 75, healpower=15, attack= 1):
        self.healpower = healpower
        self.Max_health = health
        self._current_health = self.Max_health
        self.name = name
        self.attackpower = attack

    def __repr__(self):
        return f"name:{self.name}. health:{self._current_health}. max health:{self.Max_health}. attackpower:{self.attackpower}. healpower:{self.healpower}."


    def heal(self, other):
        other.get_healed(self)

war1 = Character("jack", 100,20)
war2 = Character("max", 100, 22)
med = Healer("jess", 75, 15)

def round (war1, war2):
    war1.hit(war2)
    if war2.get_health() <= 0:
        return
    war2.hit(war1)
    if war1.get_health() <= 0:
        return

def match(rounds, fighter1,fighter2):
    for i in range(rounds):
        round(fighter1,fighter2)
        print(war1)
        print(war2)
        print()
        if fighter2.get_health() <= 0:
            return fighter1
        elif fighter1.get_health() <= 0:
            return fighter2

print(match(100,war1,war2),"wins")