# Import libraries
import turtle as guy

# Speed up program  
guy.speed(10)

# Store user inputs
height = int(input("Enter height of character:"))
guy.pensize(int(input("Enter fatness of character:")))
guy.pencolor(str(input("Enter color of character:")).lower()) # String the input value to prevent errors

# Draw
guy.circle(50)
guy.rt(90)
guy.fd(height * 10) # Scale body, arms, and legs by height variable
guy.rt(45)
guy.fd(height * 5)
guy.bk(height * 5)
guy.lt(90)
guy.fd(height * 5)
guy.bk(height * 5)
guy.rt(45)
guy.bk(height * 6)
guy.rt(135)
guy.fd(height * 4)
guy.bk(height * 4)
guy.lt(270)
guy.fd(height * 4)

# Display screen
wn = guy.Screen()
wn.mainloop()