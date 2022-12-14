"""
Exercise "The inventory sequence"

As always, read the whole exercise description carefully before your start to solve the exercise.

This exercise is an optional challenge for the excellent programmers among you.
You absolutely do not have to solve this exercise in order to proceed successfully.

Copy this file into your own solution directory. Write your solution into the copy.

Watch the first 3 minutes of this video:
https://www.youtube.com/watch?v=rBU9E-ZOZAI

Write a function "inventory" which produces the numbers shown in the video.
The function accepts a parameter defining how many number rows to produce.
The function prints out the numbers of each row.

You will probably want to define a function count_number which counts how often a certain number
appears in the current number sequence.

In the main program, call inventory with 6 as an argument.

If you have no idea how to begin, have a look at the solution in S0102_inventory.py

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

class inventorycore():
    def __init__(self):
        self.inventory = list()
        self.current_level = 0

    def layercalc(self):
        numbers = list()
        num = 0
        last = 1
        while not last == 0:
            last = self.inventory.count(num)
            numbers.append(self.inventory.count(num))
            self.inventory.append(self.inventory.count(num))
            num += 1



        return numbers

    def rerun(self,length = 0):
        for i in range(length + 1):
            layer = self.layercalc()
            self.current_level += 1
            print(layer)




iner = inventorycore()

iner.rerun(10)
print("break")
iner.rerun(5)


