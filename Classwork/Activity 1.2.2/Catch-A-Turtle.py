import turtle;from random import randint,choice;score=0;timer=3;timerUp=False;size=10;userName=input("Enter Username: ")
box=turtle.Turtle(shape="square");box.fillcolor("black");box.shapesize(10);box.penup();box.speed(0)
scoreDisplay=turtle.Turtle();scoreDisplay.penup();scoreDisplay.hideturtle();scoreDisplay.goto(-450,350)
count=turtle.Turtle();count.penup();count.hideturtle();count.goto(350,350);count.write(f"Timer: {score}",font=("Arial",20,"normal"))
def boxClicked(x,y):
    global timerUp,size,score
    if not timerUp:box.color(choice(["red","orange","yellow","green","blue","purple","pink"]));box.stamp()
    score+=int(round(1/size,2)*100);scoreDisplay.clear();scoreDisplay.write(f"Score: {score}",font=("Arial",20,"normal"))
    box.color("black");box.goto(randint(-400,400),randint(-300,300));box.shape(choice(["triangle","circle","square","turtle"]))
    size=randint(1,10);box.shapesize(size)
def drawLeaderboard(namesList,scoresList,box,score):
    box.color("black");box.clear();box.penup();box.goto(-160,100);box.hideturtle();fontSetup=("Arial",20,"normal")
    for i,name in enumerate(namesList):box.write(f"{i+1}\t{name}\t{scoresList[i]}",font=fontSetup);box.goto(-160,int(box.ycor())-50)
    msg="Congratulations!\nYou made the leaderboard!" if score in scoresList else "Sorry!\nYou didn't make the leaderboard.\nMaybe next time!"
    box.write(msg,font=fontSetup)
def countdown():
    global timer,timerUp,score,box;count.clear()
    if timer<=0:count.write("Time Up!",font=("Arial",20,"normal"));timerUp=True
    else:timer-=1;count.write(f"Time:{timer}",font=("Arial",20,"normal"));count.getscreen().ontimer(countdown,1000)
    if timer<=0:
        with open("leaderboard.txt") as f:data=[line.strip().split(",") for line in f]
        namesList,scoresList=[name for name,_ in data],[int(score) for _,score in data]
        if len(scoresList)<5 or score>=scoresList[4]:
            idx=next((i for i,s in enumerate(scoresList) if score>s),len(scoresList))
            namesList.insert(idx,userName);scoresList.insert(idx,score)
            if len(namesList)>5:namesList.pop();scoresList.pop()
            with open("leaderboard.txt","w") as f:f.writelines(f"{n},{s}\n" for n,s in zip(namesList,scoresList))
        drawLeaderboard(namesList,scoresList,box,score)
box.onclick(boxClicked);wn=turtle.Screen();wn.bgcolor("gray");wn.ontimer(countdown,1000);wn.mainloop()