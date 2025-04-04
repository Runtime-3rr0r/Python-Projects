import turtle as trtl

# create two empty lists of turtles,adding to them later
horiz_turtles=[];vert_turtles=[]
ogH=[];ogV=[]

# use interesting shapes and colors
turtle_shapes=["arrow","turtle","square","triangle","classic"]


horiz_colors=["red","blue","green","orange","purple","gold"]
vert_colors=["darkred","darkblue","lime","salmon","indigo","brown"]


hColors=["red","blue","green","orange","purple","gold"]
vColors=["darkred","darkblue","lime","salmon","indigo","brown"]


shapes=["arrow","turtle","square","triangle","classic"]

tloc=50
for s in turtle_shapes:
  ht=trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ogH.append(ht)
  ht.penup()
  new_color=horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350,tloc)
  ht.setheading(0)

  vt=trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  ogV.append(vt)
  vt.penup()
  new_color=vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc,350)
  vt.setheading(270)
  tloc += 50

hPosx=horiz_turtles[0].xcor();hPosy=horiz_turtles[0].ycor() # define positions
vPosx=vert_turtles[0].xcor();vPosy=vert_turtles[0].ycor()
speedUp=True;upperSpeed=10;lowerSpeed=5;spd=0 # set speed limit

for step in range(50):
  if speedUp:spd+=1 # speed up
  else:spd-=1

  if spd>upperSpeed:speedUp=False # if too fast,slow down
  elif spd<lowerSpeed:speedUp=True

  count=0
  for h in horiz_turtles: # horizontal turtles
    hPosx=h.xcor();hPosy=h.ycor() # get positions

    if abs(vPosx-hPosx)<=20 and abs(vPosy-hPosy)<=20: # check collisions
      horiz_turtles.pop();vert_turtles.pop()
      
      h.shape("circle");h.color("gray");v.shape("circle");v.color("gray") # show collision

      h.bk(10);v.bk(50) # recover

      h.color(hColors[count]);h.shape(shapes[count])
      v.color(vColors[count]);v.shape(shapes[count])

    if len(horiz_turtles)==0: # move after recovered
      for i in range(10):
        for h in ogH:
          h.fd(spd)
          for v in ogV:v.fd(spd)
  
      for h in ogH:
        h.color("red")
        for v in ogV:v.color("red")

    h.fd(spd);count+=1 # move

  for v in vert_turtles: # vertical turtles
    
    vPosx=v.xcor();vPosy=v.ycor() # get positions

    v.fd(spd) # move

wn=trtl.Screen();wn.mainloop()