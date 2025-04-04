from time import sleep
import turtle

healthBar=turtle.Turtle(shape="square")
healthBar.color("green")
healthBar.setheading(0)
healthBar.turtlesize(1)
healthBar.pu()
healthBar.speed(0)
healthBar.hideturtle()
health = 10

def drawHealthBar(health):
    healthBar.goto(-100,0)
    healthBar.clear()

    for i in range(0,health):
        healthBar.fd(25)
        healthBar.stamp()

while True:
    drawHealthBar(health)
    sleep(1)
    health -= 1
    if health == 0:
        break

wn=Turtle.Screen()
wn.mainloop()