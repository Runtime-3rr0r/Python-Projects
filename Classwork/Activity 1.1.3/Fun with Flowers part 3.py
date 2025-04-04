# Imports
import turtle as trtl
pt = trtl.Turtle()

# Setup
pt.speed(0)
pt.shape("circle")

for i in range(18):
    pt.fd(20)
    pt.rt(20)
    pt.stamp()

# Display persistant screen
wn = trtl.Screen()
wn.mainloop()