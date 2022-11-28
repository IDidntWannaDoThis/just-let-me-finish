"""
Exercise "Cars":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

define a function that prints a car's motor sound (for example "roooaar")

in the main program:
define variables which represent the number of wheels and the maximum speed of 2 different cars
print out these properties of both cars
then call the motor sound function

if you have no idea how to begin, open S0046_cars.py and start from there
if you get stuck, ask google, the other pupils or the teacher (in this order).
if you are still stuck, open S0047_cars.py and compare it with your solution

Compare your program to the teacher's solution in S0047_cars.py

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

class Vehicle:  # this starts the definition of a class


    def __init__(self, wheels, max_speed):
        self.wheels = wheels
        self.max_speed = max_speed
    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


car1 = Vehicle(4,160)  # car1 is now defined as an object of type Vehicle
car1.wheels = 4  # the attribute wheels is now defined for the object car1 of class Vehicle
car1.max_speed = 160  # the attribute max_speed is now defined for the object car1 of class Vehicle

car2 = Vehicle(8,100)
car2.wheels = 8
car2.max_speed = 100

print("wheels", car1.wheels, "maximum speed", car1.max_speed)  # print out the attributes of car1
print("wheels", car2.wheels, "maximum speed", car2.max_speed)  # print out the attributes of car2
car1.drive()