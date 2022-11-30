"""
Exercise: Object oriented role playing game, part 1 :

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

define a class Character with attributes name, max_health, _current_health, attackpower.
_current_health shall be a private attribute, it is not meant to be changed from outside the class

add a constructor (__init__) which accepts the classes' attributes as parameters
add a method for printing out class objects (__repr__)

add a method hit which reduces _current_health of another character by attackpower.
example: _current_health=80 and attackpower=10: a hit reduces _current_health to 70.

the method hit may not change the private attribute _current_health off a (potentially) foreign class
for this reason we define another method get_hit which reduces _current_health of the object it belongs to by attackpower.

If you get stuck, ask google, the other pupils or the teacher (in this order).
If you have no idea how to begin, open S0061_rpg1.py and start from there.

When your program is complete, push it to your github repository
and compare it to the teacher's solution in S0065_rpg1.py
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""
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
        self._current_health -= attacker.attackpower

    def get_healed(self, healer):
        self._current_health += healer.healpower

    def get_health(self):
        return self._current_health


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
war2 = Character("max", 100, 24)
med = Healer("jess", 75, 15)

print(war1)
print(war2)
print(med)
war1.hit(war2)
print(war2)
med.heal(war2)
print(war2)