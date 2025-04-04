import turtle;from random import randint,choice;s,t,tU,sz,sD,u=0,3,False,10,turtle.Turtle(),input("Enter username: ")
b,c=turtle.Turtle(shape="square"),turtle.Turtle();b.fillcolor("black");b.shapesize(10);b.penup();b.speed(0)
sD.penup();sD.hideturtle();sD.goto(-450,350);c.penup();c.hideturtle();c.goto(350,350);c.write(f"Timer: {s}",
font=("Arial",20,"normal"))
def bC(x,y):
    global tU,sz,s
    if not tU:b.color(choice(["red","orange","yellow","green","blue","purple","pink"]));b.stamp()
    s+=int(round(1/sz,2)*100);sD.clear();sD.write(f"Score: {s}",font=("Arial",20,"normal"));b.color("black")
    b.goto(randint(-400,400),randint(-300,300));b.shape(choice(["triangle","circle","square","turtle"]))
    sz=randint(1,10);b.shapesize(sz)
def dL(nL,sL,b,s):
    b.color("black");b.clear();b.penup();b.goto(-160,100);b.hideturtle();fS=("Arial",20,"normal")
    for i,name in enumerate(nL):b.write(f"{i+1}\t{name}\t{sL[i]}",font=fS);b.goto(-160,int(b.ycor())-50)
    msg="You made the leaderboard!" if s in sL else "You didn't make the leaderboard!";b.write(msg,font=fS)
def countdown():
    global t,tU,s,b;c.clear()
    if t<=0:
        c.write("Time Up!",font=("Arial",20,"normal"));tU=True
        with open("leaderboard.txt") as f:data=[line.strip().split(",") for line in f]
        nL,sL=[name for name,_ in data],[int(s) for _,s in data]
        if len(sL)<5 or s>=sL[4]:
            idx=next((i for i,s in enumerate(sL) if s>s),len(sL));nL.insert(idx,u);sL.insert(idx,s)
            if len(nL)>5:nL.pop();sL.pop()
            with open("leaderboard.txt","w") as f:f.writelines(f"{y},{z}\n" for y,z in zip(nL,sL))
        dL(nL,sL,b,s)
    else:t-=1;c.write(f"Time:{t}",font=("Arial",20,"normal"));c.getscreen().ontimer(countdown,1000)
b.onclick(bC);wn=turtle.Screen();wn.bgcolor("gray");wn.ontimer(countdown,1000);wn.mainloop()