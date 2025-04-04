# Imports
import turtle as trtl
pt = trtl.Turtle()

# Draw square
for i in range(4):
    pt.fd(50)
    pt.rt(90)

# Move painter
pt.penup()
pt.goto(100,100)
pt.pendown()

# Draw octogon
for i in range(8):
    pt.fd(50)
    pt.rt(360/8)

# Display persistant screen
wn = trtl.Screen()
wn.mainloop()