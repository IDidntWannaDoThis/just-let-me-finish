"""
Exercise "Reading from a file":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

create a text file with a editor of your choice (pycharm, notepad, notepad++, etc.)
each row shall consist of a person's name, followed by a space and a number, representing the person's age.
save the file in a subdirectory "data" of your solution directory

write a program which reads the file into a list of strings
then use the content of each string to print out a row like:
    <name> is <age> years old.

if you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

myfile = "data/people.txt"
print("what is your name?")
name = input()
print("how old are you, "+name)
age = input()
with open(myfile) as file:  # when the program exits the with-block, the file is automatically closed
    lines = file.readlines()
with open(myfile, "w") as file:
    for line in lines:
        file.write(line)
    file.write(f"{name} is {age} years old. \n")

line_number = 0
with open(myfile) as file:
    for line in file:
        line_number += 1
        print(f"Line {line_number}: {line.strip()}")
    print()


