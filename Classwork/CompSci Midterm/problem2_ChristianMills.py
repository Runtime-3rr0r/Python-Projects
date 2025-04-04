# problem2_ChristianMills.py

# imports
import turtle

# make a turtle
pt=turtle.Turtle(shape="turtle")
pt.color("black")

# draw square
for i in range(4):
    pt.fd(25)
    pt.rt(90)

# reposition
pt.pu()
pt.fd(50)
pt.rt(90)
pt.pd()

# draw rectangle
for i in range(2):
    pt.fd(50)
    pt.rt(90)
    pt.fd(75)
    pt.rt(90)
    pt.fd(50)

# persist screen
wn=turtle.Screen()
wn.mainloop()