# imports
import turtle
import leaderboard as lb
from random import randint,choice

# game init
color="black"
size=10
shape="square"
score=0
fontSetup=("Arial",20,"normal")
timer=30
timerUp=False
fileName="leaderboard.txt"
userName=input("Enter Username: ")

# turtle init
box=turtle.Turtle(shape=shape)
box.fillcolor(color)
box.shapesize(size)
box.penup()
box.speed(0)

scoreDisplay=turtle.Turtle()
scoreDisplay.penup()
scoreDisplay.hideturtle()
scoreDisplay.goto(-450,350)

count=turtle.Turtle()
count.penup()
count.hideturtle()
count.goto(350,350)
count.write("Timer: "+str(score),font=fontSetup)

# events
def boxClicked(x,y):
    global timerUp
    
    if not timerUp:
        box.color(choice(["red","orange","yellow","green","blue","purple","pink"]))
        box.stamp()

    updateScore()
    moveBox()
    changeBox()

def updateScore():
    global score

    score+=int(round(1/size,2)*100)
    scoreDisplay.clear()
    scoreDisplay.write("Score: "+str(score),font=fontSetup)

def moveBox():
    box.color("black")
    box.goto(randint(-400,400),randint(-300,300))

def changeBox():
    global size

    box.shape(choice(["triangle","circle","square","turtle"]))
    size=randint(1,10)
    box.shapesize(size)
    
def countdown():
    global timer,timerUp
    
    count.clear()
    if timer<=0:
        count.write("Time Up!",font=fontSetup)
        box.hideturtle()
        timerUp=True
    else:
        timer-=1
        count.write("Time: "+str(timer),font=fontSetup)
        count.getscreen().ontimer(countdown,1000)

# main
box.onclick(boxClicked)
wn=turtle.Screen()
wn.bgcolor("gray")
wn.ontimer(countdown,1000)
wn.mainloop()