"""
Exercise "Number guessing"

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Create a program that will play a number guessing game with the user. The program works like this:
    Explain the rules to the user.
    Randomly generate a 4-digit integer number.
    Ask the user to guess a 4-digit number.
    Every digit that the user guesses correctly in the correct position, counts as a black coin.
    Every digit the user guesses correctly, but in the wrong position, counts as a white coin.
    After the user made a guess, print out how many black and white coins the guess is worth.
    let the user guess until the guess is correct.
    Keep track of the number of guesses the user makes throughout the game and print it out at the end.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

import random

class numguessgame():
    def __init__(self):
        self.numbers = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]
        self.win = False
        self.rounds = 0

    def rond(self):
        print("what numbers are in the string")
        number = input()
        for i in range(4):
            if number.__getitem__(i) == str(self.numbers[i]):
                yield "true"
            else:
                if self.numbers.__contains__(int(number.__getitem__(i))):
                    yield "else"
                else:
                    yield "false"

    def wincheck(self, score):
        truescore = 0
        for part in score:
            if part == "true":
                truescore += 1
        if truescore == 4:
            return True
        else:
            return False


    def play(self):
        if self.win:
            print(f"this game was won in {self.rounds} rounds")
        while not self.win:
            self.rounds += 1
            level = list(self.rond())
            print(level)
            self.win = self.wincheck(level)
        print(self.numbers)
        print(f"you won in {self.rounds} turns")


    def restart(self):
        self.numbers = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
        self.win = False
        self.rounds = 0



numguessgame1 = numguessgame()
numguessgame1.play()
numguessgame1.restart()
numguessgame1.play()
