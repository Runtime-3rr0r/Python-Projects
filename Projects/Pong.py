#!/usr/bin/env python3

"""
Name: Pong.py
Project Number: 5
Author: Christian M
Date: Aug 6, 2022
"""

import turtle

win = turtle.Screen()
win.title("Pong by Christian M")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

score_a = 0
score_b = 0

net = turtle.Turtle()
net.shape("square")
net.color("#808080")
net.shapesize(stretch_wid=30, stretch_len=0.5)
net.penup()
net.goto(0, 0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#FFFFFF")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#FFFFFF")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#FFFFFF")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.25
ball.dy = 0.25

pen = turtle.Turtle()
pen.speed(0)
pen.color("#FFFFFF")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  Computer: {score_b}", align="center",
          font=("Consolas", 24, "normal"))

def paddle_a_up():
    
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    
    y = paddle_b.ycor()
    y += 0.2
    paddle_b.sety(y)


def paddle_b_down():
    
    y = paddle_b.ycor()
    y -= 0.2
    paddle_b.sety(y)


def follow_ball():
    
    if paddle_b.ycor() < ball.ycor():
        paddle_b_up()
    
    if paddle_b.ycor() > ball.ycor():
        paddle_b_down()


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")

while True:
    follow_ball()

    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        
        ball.goto(0, 0)
        ball.dx *= -1
        
        score_a += 1
        
        pen.clear()
        pen.write(f"Player A: {score_a}  Computer: {score_b}", align="center",
                  font=("Consolas", 24, "normal"))


    if ball.xcor() < -390:
        
        ball.goto(0, 0)
        ball.dx *= -1
        
        score_b += 1
        
        pen.clear()
        pen.write(f"Player A: {score_a}  Computer: {score_b}", align="center",
                  font=("Consolas", 24, "normal"))


    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()
            < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        
        ball.setx(340)
        ball.dx *= -1
    
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()
            < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        
        ball.setx(-340)
        ball.dx *= -1