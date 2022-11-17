"""
Exercise "Tom the Turtle":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

The function "demo" introduces you to all commands you need to interact with Tom in the following exercises.

Only if you are curious and love details:
    Here is the full turtle graphics documentation:
    https://docs.python.org/3.3/library/turtle.html

Part 1:
    Write a function "square" which accepts a parameter "length".
    Calling this function causes the turtle to draw a square with a side length of "length" pixels.

Part 2:
     Write a function "visible" which returns a boolean value,
     indicating if the turtle is in the visible area of the screen.
     Use this function in the following parts of this exercise
     to return the turtle to the screen when it wandered off.

Part 3:
    Write a function "many_squares" with a for loop, which calls square repeatedly.
    Use this function to draw several squares of different sizes in different positions.
    The function shall have some parameters. For example:
        number: how many squares will be drawn?
        size: how large are the squares?
        distance: how far away from the last square is the next square positioned?

Part 4:
    Write a function that produces patterns similar to this:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Part 5:
    Write a function that produces patterns similar to this:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    The function shall have a parameter, that influences the shape of the pattern.

Part 6:
    Create your own function that produces a cool pattern.
    Later, if you like, present your pattern on the big screen to the others.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""
import random
import turtle    # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):
        tom.forward(100)  # move 100 pixels
        tom.left(45)  # turn 45 degrees left
        print("Tom is now at", tom.position())
    tom.penup()  # do not draw while moving
    tom.forward(222)
    tom.pendown()  # draw while moving
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(333)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  #keeps the turtle window open after the program is done

def square(length,body):
    tim = body
    print(type(tim))
    tim.speed(1)
    for x in range(4):
        tim.forward(length)
        if not isonscreen(tim):
            while not isonscreen(tim):
                tim.backward(1)
                print("Tim is now at", tim.position())
                tim.backward(1)
        tim.left(90)
        print("Tim is now at", tim.position())

def isonscreen(body):
    if body.getscreen().window_width() / 2 > body.xcor() and body.getscreen().window_height() / 2 >  body.ycor():
        return True
    else:
        return False

def many_square(reapeated,size,distrnce,body):
    for x in range(reapeated):
        square(random.randint(0,size,),body)
        body.penup()
        body.right(random.randint(0, 360))
        body.forward(distrnce)
        body.pendown()


def spyral(size,body):
    for x in range(size) :
        body.forward(10*(x+1))
        body.left(90)

def star(points,body):
    for x in range(points):
        body.forward(100)
        body.left(720 / points)







star(5,turtle.Turtle())
turtle.done()

