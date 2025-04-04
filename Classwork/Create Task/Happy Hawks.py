"""
Happy Hawks.py

By:           John Eoh and Christian Mills
Project:      AP Create Task
Date Created: 3/28/2025
Date Final:   TBD

Description:  Target practice game inspired by "Angry Birds"
"""

# imports
from random import randint
from time import sleep
from math import sqrt
import turtle

# global variables
slingshotX = -300
targetRange = 0
slingshotY = 50
xVelocity = 0
yVelocity = 0

released = False
flying = False
game = True

setup(diffculty):

    # global variables
    global targetRange

    # adjust target ranged for difficulty
    if difficulty == "1":
        targetRange = 50
    elif difficulty == "2":
        targetRange = 35
    else:
        targetRange = 20

    # setup turtles
    wn = turtle.Screen()
    turtleImages = ["slingshot.gif", "bird.gif", "target.gif"]

    # iterate over saved turtle images and add them to program
    for image in turtleImages:
        wn.addshape(image)

    hawk = turtle.Turtle(shape="circle")
    hawk.color("black")
    hawk.turtlesize(2)
    hawk.speed(0)
    hawk.pu()
    hawk.goto(slingshotX, slingshotY)

    slingshot = turtle.Turtle(shape="triangle")
    slingshot.color("brown")
    slingshot.speed(0)
    slingshot.pu()
    slingshot.goto(slingshotX, slingshotY)

    target = turtle.Turtle(shape="square")
    target.color("red")
    target.turtlesize(2)
    target.speed(0)
    target.pu()
    target.goto(randint(150, 400), 0)

    lastPath = turtle.Turtle(shape="circle")
    lastPath.color("grey")
    lastPath.speed(0)
    lastPath.pu()
    lastPath.ht()
    lastPath.goto(randint(150, 400), 0)

def drag(mouseX, mouseY):

    if not released:

        if mouseX > slingshotX or mouseX < slingshotX - 100: mouseX = hawk.xcor()

        if mouseY < slingshotY - 100 or mouseY > slingshotY + 100: mouseY = hawk.ycor()

        hawk.goto(mouseX, mouseY)
   
    hawk.ondrag(drag)


def release(_x, _y):

    # global variables
    global xVelocity
    global yVelocity
    global released

    released = True

    # calculate flight variables
    hawkDistanceX = slingshotX - hawk.xcor()
    hawkDistanceY = slingshotY - hawk.ycor()

    xVelocity = hawkDistanceX * 0.8
    yVelocity = hawkDistanceY * 0.75


def isCollision(a, b):
    return abs(a.xcor() - b.xcor()) < 40


def fly(xVelocity, yVelocity):

    # global variables
    global flying

    # local variables
    gravity = -9.81
    deltaTime = 0.2
    moveCount = 0
    time = 0

    posX = hawk.xcor()
    posY = hawk.ycor()

    flying = True

    # animate flight path and update flight variables
    while True:
        
        time += deltaTime
        posX += xVelocity * deltaTime
        posY += yVelocity * deltaTime + 0.5 * gravity * deltaTime ** 2
        yVelocity += gravity * deltaTime

        if moveCount % 8 == 0 and posX > slingshotX + 20: lastPath.stamp()

        if posY <= 0 and posX > slingshotX:
            yVelocity = -yVelocity * 0.7
            xVelocity = xVelocity * 0.6

        hawk.goto(posX, posY)
        lastPath.goto(posX, posY)

        if abs(xVelocity) + abs(yVelocity) <= 2 and posY <= 2: break

        moveCount += 1

    # calculate velocity
    return sqrt(xVelocity ** 2 + yVelocity ** 2)

# main
while game:
    drag(hawk.xcor(), hawk.ycor())
    hawk.onrelease(release)

    if released and not flying:
        fly(xVelocity, yVelocity)

wn.mainloop()