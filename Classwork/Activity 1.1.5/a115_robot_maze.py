# a115_rob_maze.py
import turtle as trtl

# maze/turtle config vars
screenH=400
screenW=420
startX=-100
startY=-100
turtleScale=1.5

# rob commands
def move(dist=1):
  for i in range(dist):
    rob.dot(10)
    rob.fd(50)

def turnLeft(times=1):
  for i in range(times):
    rob.speed(0)
    rob.lt(90)
    rob.speed(2)

def turnRight(times=1):
  for i in range(times):
    rob.speed(0)
    rob.rt(90)
    rob.speed(2)

# init screen
wn=trtl.Screen()
wn.setup(width=screenW,height=screenH)
rob_image="robot.gif"
wn.addshape(rob_image)

# init rob
rob=trtl.Turtle(shape=rob_image)
rob.hideturtle()
rob.color("darkorchid")
rob.pencolor("darkorchid")
rob.penup()
rob.setheading(90)
rob.turtlesize(turtleScale,turtleScale)
rob.goto(startX,startY)
rob.speed(2)
rob.showturtle()

# TODO: change maze
wn.bgpic("modifiedMaze.png")

# TODO: begin rob movement
turnRight()
move(4)
for i in range(2):
  turnLeft();move(2)
move(2)
for i in range(2):
  turnRight();move(2)
move(2)
#---- end rob movement 

wn.mainloop()