from random import randint;import turtle;import math
def setupTurtle(turtle, x, y, color="black", shape="triangle"):
    turtle.shape(shape);turtle.color(color);turtle.speed(0);turtle.pu();turtle.goto(x,y)
time=.0;xPos=-450.0;yPos=.0;maxY=.0;initVel=50;initAng=30;xVel=initVel*math.cos(math.radians(initAng))
yVel=initVel*math.sin(math.radians(initAng));grav=-9.81;dTime=.2;frict=1;ball=turtle.Turtle();setupTurtle(ball,0,0,"black","circle")
ball.width(5);flyTime=turtle.Turtle();flyTime.ht();setupTurtle(flyTime,-195,-350);rangE=turtle.Turtle();setupTurtle(rangE,-195,-375)
rangE.ht();height=turtle.Turtle();height.ht();setupTurtle(height,-195,-400);dInitAng=turtle.Turtle();setupTurtle(dInitAng,-195,165);dInitAng.ht()
dInitAng.write(str(initAng)+"°",align="center",font=("Courier",12,"normal"));displayinitVel=turtle.Turtle();setupTurtle(displayinitVel,-95,165)
displayinitVel.ht();displayinitVel.write(str(initVel)+"m/s",align="center",font=("Courier",12,"normal"));displaygrav=turtle.Turtle()
setupTurtle(displaygrav,5,165);displaygrav.ht();displaygrav.write(str(grav)+"m/s",align="center",font=("Courier",12,"normal"))
dDrag=turtle.Turtle();setupTurtle(dDrag,105,165);dDrag.ht();dDrag.write(str(frict),align="center",font=("Courier",12,"normal"))
initAngU=turtle.Turtle();setupTurtle(initAngU,-200,150,"green");initAngU.lt(90);initAngD=turtle.Turtle();setupTurtle(initAngD,-200,130,"red")
initAngD.rt(90);initialSpeedUp=turtle.Turtle();setupTurtle(initialSpeedUp,-100,150,"green");initialSpeedUp.lt(90);initialSpeedDown=turtle.Turtle()
setupTurtle(initialSpeedDown,-100,130,"red");initialSpeedDown.rt(90);gravUp=turtle.Turtle();setupTurtle(gravUp,0,150,"green");gravUp.lt(90)
gravD=turtle.Turtle();setupTurtle(gravD,0,130,"red");gravD.rt(90);dragU=turtle.Turtle();setupTurtle(dragU,100,150,"green");dragU.lt(90)
dragD=turtle.Turtle();setupTurtle(dragD,100,130,"red");dragD.rt(90);run=turtle.Turtle();setupTurtle(run,200,140,"blue","square")
runn=turtle.Turtle();setupTurtle(runn,220,140,"blue","square");clr=turtle.Turtle();setupTurtle(clr,300,140,"gray","square");clrr=turtle.Turtle()
setupTurtle(clrr,320,140,"gray","square")

def simulateBall(x,y):
    global time;global xPos;global yPos;global maxY;global initVel;global initAng;global xVel;global yVel;global grav;global dTime
    global dragCoeff;time=.0;xPos=-450.0;yPos=.0;maxY=.0;xVel=initVel*math.cos(math.radians(initAng));yVel=initVel*math.sin(math.radians(initAng))
    dragCoeff=0;ball.pu();ball.goto(xPos,yPos);ball.pd()
    
    while True:
        time+=dTime
        xPos+=xVel*dTime
        yPos+=yVel*dTime+.5*grav*dTime**2
        yVel+=grav*dTime
        ball.goto(xPos,yPos)

        if yPos <= 0:
            yVel = -yVel * frict * (randint(8, 10) / 10) if frict < 1 else -yVel
            xVel*=frict*(randint(5,10)/10) if frict<1 else frict
            yPos=0;ball.goto(xPos,yPos)
        if xPos>=450:
            xVel=-xVel*frict*(randint(8,10)/10)if frict<1 else-xVel
            yVel*=frict*(randint(5,10)/10)if frict<1 else frict
            xPos=450;ball.goto(xPos,yPos)
        if xPos<=-460:
            xVel=-xVel*frict*(randint(8,10)/10)if frict<1 else-xVel
            yVel*=frict*(randint(5,10)/10)if frict<1 else frict
            xPos=-460;ball.goto(xPos,yPos)
        if abs(xVel)+abs(yVel)<=2 and yPos<=2:break
        maxY=yPos if yPos>maxY else maxY 
        
         
    flyTime.clear();flyTime.write("Time: "+str(round(time,2))+"s",align="left",font=("Courier",12,"normal"));rangE.clear();rangE.write("Range: "+
str(round(xPos,2)),align="left",font=("Courier",12,"normal"));height.clear();height.write("Max height: "+str(round(maxY,2)),align="left",
font=("Courier",12,"normal"))
def clearAll(x,y):ball.clear()
def increaseAngle(x,y):global initAng;initAng+=5;dInitAng.clear();dInitAng.write(str(initAng)+"°",align="center",font=("Courier",12,"normal"))
def decreaseAngle(x,y):global initAng;initAng-=5;dInitAng.clear();dInitAng.write(str(initAng)+"°",align="center",font=("Courier",12,"normal"))
def increaseVelocity(x,y):global initVel;initVel+=5;displayinitVel.clear();displayinitVel.write(str(initVel)+"m/s",align="center",font=("Courier",
12,"normal"))
def decreaseVelocity(x,y):
    global initVel
    if initVel>=5:initVel-=5
    displayinitVel.clear();displayinitVel.write(str(initVel)+"m/s",align="center",font=("Courier",12,"normal"))
def increasegrav(x,y):global grav;grav-=.1;displaygrav.clear();displaygrav.write(str(round(grav,2))+"m/s",align="center",font=("Courier",12,
"normal"))
def decreasegrav(x,y):
    global grav
    if grav<0:grav+=.1
    displaygrav.clear();displaygrav.write(str(round(grav,2))+"m/s",align="center",font=("Courier",12,"normal"))
def increaseDrag(x,y):
    global frict
    if frict<1:frict+=.1
    dDrag.clear();dDrag.write(str(round(frict,2)),align="center",font=("Courier",12,"normal"))
def decreaseDrag(x,y):
    global frict
    if frict>.2:frict-=.1
    dDrag.clear();dDrag.write(str(round(frict,2)),align="center",font=("Courier",12,"normal"))
run.onclick(simulateBall);runn.onclick(simulateBall);clr.onclick(clearAll);clrr.onclick(clearAll);initAngU.onclick(increaseAngle)
initAngD.onclick(decreaseAngle);initialSpeedUp.onclick(increaseVelocity);initialSpeedDown.onclick(decreaseVelocity);gravUp.onclick(increasegrav)
gravD.onclick(decreasegrav);dragU.onclick(increaseDrag);dragD.onclick(decreaseDrag);wn=turtle.Screen();wn.mainloop()