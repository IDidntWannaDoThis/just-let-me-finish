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

def drive_car():
    print("wroom")  # print a sound


car1_wheels = 4  # define number of wheels for car1
car1_speed = 5  # define maximum speed for car1
car2_wheels = 4  # define number of wheels for car2
car2_speed = 7  # define maximum speed for car2

print("wheels:", car1_wheels, ". max speed", car1_speed) # print out the properties of car1
print("wheels:", car2_wheels, ". max speed", car2_speed)  # print out the properties of car2

drive_car()  # call drive_car
