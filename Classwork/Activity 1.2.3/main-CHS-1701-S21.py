#-----imports-----
import turtle
from string import ascii_lowercase
from random import randint,shuffle

#-----setup-----
apple_image="apple.gif"

wn=turtle.Screen()
wn.setup(width=600,height=400)
wn.bgpic("background.gif")
wn.addshape(apple_image)

alphabet=list(ascii_lowercase)
shuffle(alphabet)

apples=[turtle.Turtle() for i in range(5)]
apple_letters=[alphabet[i] for i in range(len(apples))]

# TODO pop off letters after they are used

halt=False

#-----functions-----
def drawApple(active_apple,active_apple_letter):
  active_apple.shape(apple_image) # setup apple
  active_apple.penup()
  active_apple.hideturtle()
  active_apple.speed(0)
  active_apple.color("white")
  active_apple.setheading(270)
  
  active_apple.goto(randint(-120,120),randint(0,120)) # move apple to tree
  active_apple.stamp()

  active_apple.fd(35) # move to draw letter and go back
  active_apple.write(active_apple_letter,align="center",font=("Arial",40,"normal"))
  active_apple.bk(35)

def appleFall(apple_index):
  global halt

  halt=True
  active_apple_letter=apple_letters[apple_index]
  active_apple=apples[apple_index]

  while active_apple.ycor()>=-125:
    active_apple.fd(5)
    active_apple.clear()
    active_apple.stamp()

    active_apple.fd(35)
    active_apple.write(active_apple_letter,align="center",font=("Arial",40,"normal"))
    active_apple.bk(35)

def appleClicked(letter):
  global halt
  if letter in apple_letters and not halt:
    appleFall(apple_letters.index(letter)) # turn letter into letter index, corresponding to apple in apple index
    if len(apple_letters)>0:
      drawApple(apples[apple_letters.index(letter)],apple_letters[apple_letters.index(letter)])
    else:pass # TODO make apples disappear when they hit floor
    # TODO 
    halt=False

#-----function calls-----
for i in range(len(apples)):
  drawApple(apples[i-1],apple_letters[i-1])

def a():appleClicked("a")
wn.onkeypress(a,"a")
def b():appleClicked("b")
wn.onkeypress(b,"b")
def c():appleClicked("c")
wn.onkeypress(c,"c")
def d():appleClicked("d")
wn.onkeypress(d,"d")
def e():appleClicked("e")
wn.onkeypress(e,"e")
def f():appleClicked("f")
wn.onkeypress(f,"f")
def g():appleClicked("g")
wn.onkeypress(g,"g")
def h():appleClicked("h")
wn.onkeypress(h,"h")
def i():appleClicked("i")
wn.onkeypress(i,"i")
def j():appleClicked("j")
wn.onkeypress(j,"j")
def k():appleClicked("k")
wn.onkeypress(k,"k")
def l():appleClicked("l")
wn.onkeypress(l,"l")
def m():appleClicked("m")
wn.onkeypress(m,"m")
def n():appleClicked("n")
wn.onkeypress(n,"n")
def o():appleClicked("o")
wn.onkeypress(o,"o")
def p():appleClicked("p")
wn.onkeypress(p,"p")
def q():appleClicked("q")
wn.onkeypress(q,"q")
def r():appleClicked("r")
wn.onkeypress(r,"r")
def s():appleClicked("s")
wn.onkeypress(s,"s")
def t():appleClicked("t")
wn.onkeypress(t,"t")
def u():appleClicked("u")
wn.onkeypress(u,"u")
def v():appleClicked("v")
wn.onkeypress(v,"v")
def w():appleClicked("w")
wn.onkeypress(w,"w")
def x():appleClicked("x")
wn.onkeypress(x,"x")
def y():appleClicked("y")
wn.onkeypress(y,"y")
def z():appleClicked("z")
wn.onkeypress(z,"z")

wn.listen()
wn.mainloop()