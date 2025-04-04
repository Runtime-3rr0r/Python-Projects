# imports
import turtle
import math
from random import randint

# setup turtle
projectile=turtle.Turtle(shape="circle")
projectile.color("black")

# vars (defaults)
time = 0.00
xPos = -450.00
yPos = 0.00
maxY = 0.00
bouncyBallCount = 0
initialVelocity = 50
initialAngle = 30
xVelocity = initialVelocity * math.cos(math.radians(initialAngle))
yVelocity = initialVelocity * math.sin(math.radians(initialAngle))
xAcceleration = 0
yAcceleration = -9.81
deltaTime = 0.2

# setup path
projectile.pu()
projectile.goto(xPos, yPos)
projectile.pd()

# main sim loop
while yPos >= 0:
    time += deltaTime
    xPos += xVelocity * deltaTime
    yPos += yVelocity * deltaTime + 0.5 * yAcceleration * deltaTime * deltaTime
    yVelocity += yAcceleration * deltaTime
    projectile.goto(xPos, yPos)

    maxY = yPos if yPos > maxY else maxY
        

print("Time of flight: ", round(time, 2))
print("Range: ", round(xPos, 2))
print("Max height: ", round(maxY, 2))
print("bouncy ball count:", bouncyBallCount)

wn=turtle.Screen()
wn.mainloop()