import turtle as trt
painter = trt.Turtle()

# Modifiers
painter.turtlesize(3)
painter.pensize(5)
painter.speed(5)

# Square loop
for i in range(4):
    painter.forward(100)
    painter.right(90)

# Main
wn = trt.Screen()
wn.mainloop()