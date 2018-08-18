import turtle,time
t=turtle.Screen()
t.setup(width=800, height=700)
t.title("Pong game By Saurabh Jadhav")

t.bgcolor("black")
#intro
intro=turtle.Turtle()
intro.goto(0,0)
intro.color("white")
intro.hideturtle()
intro.write("Pong game",font=("Courier",26),align="center")
intro.sety(-29)
intro.write("By Saurabh Jadhav",font=("Courier",26),align="center")

time.sleep(2)


#player 1
pen=turtle.Turtle("square")
pen.speed(0)
pen.turtlesize(4,0.5)
pen.color("red")
pen.up()
pen.goto(-290,0)
#player 2
pen2=turtle.Turtle("square")
pen2.speed(0)
pen2.color("red")
pen2.turtlesize(4,0.5)

pen2.up()
pen2.goto(290,0)
time.sleep(1.5)
#hide intro
intro.clear()

#border
b=turtle.Turtle()
b.color("white")
b.up()
b.goto(-340,290)




for border in range(2):
	b.speed(0)
	b.down()
	b.forward(700)
	b.right(90)
	b.forward(600)
	b.right(90)
#trying second border
b.goto(-350,300)

for border in range(2):
	b.speed(0)
	b.down()
	b.forward(700)
	b.right(90)
	b.forward(600)
	b.right(90)

#middle line
m1=turtle.Turtle()
m1.color("white")
m1.right(90)
m1.forward(250)
m1.backward(250)
m1.right(180)
m1.forward(250)

#score
score_a=0
score_b=0
score=turtle.Turtle()
score.color("white")
score.speed(0)
score.sety(240)
score.hideturtle()
score.write("Player A = 0 and Player B = 0 ",font=("Times",19,"bold"),align="center")
name=turtle.Turtle()
name.goto(6,300)
name.color("white")
name.write("Made By Saurabh Jadhav",font=("Times",14,"bold"),align="center")

#player
p1pos=0
p2pos=0
def p1movup():
	global p1pos
	xx=pen.ycor()
	print(xx)
	if xx==250:
		pass
	else:
		
		p1pos+=50
		pen.sety(p1pos)

	
def p1movdown():
	global p1pos
	yy=pen.ycor()
	print(yy)
	if yy==-250:
		pass
	else:
		p1pos-=50
		pen.sety(p1pos)

def p2movup():
	global p2pos
	xx1=pen2.ycor()
	if xx1==250:
		pass
	else:
		p2pos+=50
		pen2.sety(p2pos)
def p2movdown():
	global p2pos
	yy1=pen2.ycor()
	if yy1==-250:
		pass
	else:
		pen2.up()
		p2pos-=50
		pen2.sety(p2pos)


t.listen()

t.onkeypress(p1movup,"q")
t.onkeypress(p1movdown,"a")

t.onkeypress(p2movup,"Up")
t.onkeypress(p2movdown,"Down")
#ball

bll=turtle.Turtle("circle")
bll.color("white")
bll.speed(0)
bll.up()
bll.dx=5
bll.dy=-5 
done=0
def check():
	done=1
t.onkey(check,"z")

def move():
	
	global score_a,score_b
	while done==0:
		bll.setx(bll.xcor()+bll.dx)
		bll.sety(bll.ycor()+bll.dy)
		#border check
		if bll.ycor()>290:
			bll.sety(290)
			bll.dy*=-1
		if bll.ycor()<-290:
			bll.sety(-290)
			bll.dy*=-1
		if bll.xcor()>340:
			bll.goto(0,0)
			bll.dx*=-1
			score_a+= 1
			score.clear()
			score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


		if bll.xcor()<-340:
			bll.goto(0,0)
			bll.dx*=-1
			score_b += 1
			score.clear()
			score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



		if (bll.xcor() > 280 and bll.xcor() < 290) and (bll.ycor() < pen2.ycor() + 80 and bll.ycor() > pen2.ycor() - 80):
			bll.setx(280)
			bll.dx*=-1
		if (bll.xcor() < -280 and bll.xcor() > -290) and (bll.ycor() < pen.ycor() + 80 and bll.ycor() > pen.ycor() - 80):
			bll.setx(-280)
			bll.dx*=-1
move()
t.mainloop()	