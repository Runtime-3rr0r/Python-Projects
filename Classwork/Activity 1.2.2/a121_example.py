# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
raphael_color = "crimson"
raphael_shape = "turtle"
raphael_size = 5
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
raphael = trtl.Turtle()
raphael.fillcolor(raphael_color)
raphael.shape(raphael_shape)
raphael.turtlesize(raphael_size)
raphael.penup()
raphael.speed(0)
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-450, 370)
counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(320,370)

#-----game functions--------
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write("Score = " + str(score), font=font_setup)
def change_position():
    new_x = rand.randint(-400,400)
    new_y = rand.randint(-400,400)
    raphael.goto(new_x, new_y)
def raphael_clicked(x, y):
    global timer_up
    if timer_up:
        raphael.hideturtle()
    else:
        raphael.hideturtle()
        change_position()
        raphael.showturtle()
        update_score()
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    raphael.hideturtle()
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

    
#-----events----------------
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
raphael.onclick(raphael_clicked)
wn.mainloop()