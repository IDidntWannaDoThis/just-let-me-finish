"""
Exercise "Morris The Miner" (this time object oriented)

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Rewrite your original Morris code into an object oriented version.

Define a class Miner with attributes like sleepiness, thirst, etc.
and methods like sleep, drink, etc.
Create Morris and initialize his attributes by calling the constructor of Miner:
morris = Miner()

If you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""
class miner:
        def __init__(self,):
            self.exaust = 0
            self.whisky = 0
            self.thirst = 0
            self.hunger = 0
            self.gold = 0
            self.age = 0
        
        def sleep(self):
            self.exaust -= 10
            self.thirst += 1
            self.hunger += 1
            print("you had a good nights sleep")
            self.age += 1
            return

        def mine(self):
            self.exaust += 5
            self.gold += 5
            self.thirst += 5
            self.hunger += 5
            print("you went mining and found some gold")
            self.age += 1
            return

        def eat(self):
            if self.gold >= 2:
                self.exaust += 5
                self.gold -= 2
                self.hunger -= 20
                self.thirst -= 5
                self.age += 1
                print("you ate some food")
            else:
                print("you don't have Enough gold")
            return

        def drink(self):
            if self.whisky >= 1:
                self.exaust += 5
                self.whisky -= 1
                self.thirst -= 15
                self.hunger -= 1
                self.age += 1
                print("you drank a bottle of whisky")

            else:
                print("you don't have any whisky")

            return

        def buy(self):
            if self.gold >= 1:
                self.exaust += 5
                self.gold -= 1
                self.whisky += 1
                self.thirst += 1
                self.age += 1
                print("you bought a bottle of whisky")
            else:
                print("you don't have Enough gold")


            return

        def deathcheck(self):
            if self.thirst >= 100:
                print("you died of thirst")
                death = True
            elif self.hunger >= 100:
                print("you died of starvation")
                death = True
            elif self.exaust >= 100:
                print("you died of exaustion")
                death = True
            else:
                death = False

            return death

def CP(miner):
    if miner.thirst > 90:
        if miner.hunger > 90 and miner.gold > 1:
            miner.eat()
        elif miner.whisky >= 1:
            miner.drink()
        else:
            miner.mine()
    elif miner.hunger > 90 and miner.gold > 1:
        miner.eat()
    elif miner.whisky < 1 and miner.gold > 0:
        miner.buy()
    elif miner.exaust > 75:
        miner.sleep()
    else:
        miner.mine()

def life(miner):
    while miner.age <= 1000 and not miner.deathcheck():
        CP(miner)

        print(f"you died with {miner.gold} gold")
morris = miner()
life(morris)