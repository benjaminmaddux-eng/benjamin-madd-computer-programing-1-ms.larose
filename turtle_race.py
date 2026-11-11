#benjamim maddux computer programing ms.larose
import turtle
import random
widow=turtle.Screen()
widow.bgcolor("tan")
line=turtle.Turtle()



tR=turtle.Turtle()
tR.penup()
tR.shape("turtle")
tR.color("red")
tR.goto(-400,370)
tR.pendown()



tP=turtle.Turtle()
tP.penup()
tP.shape("turtle")
tP.color("purple")
tP.goto(-400,210)
tP.pendown()



tY=turtle.Turtle()
tY.penup()
tY.shape("turtle")
tY.color("yellow")
tY.goto(-400,50)
tY.pendown()



tG=turtle.Turtle()
tG.penup()
tG.shape("turtle")
tG.color("green")
tG.goto(-400,-120)
tG.pendown()



tB=turtle.Turtle()
tB.penup()
tB.shape("turtle")
tB.color("blue")
tB.goto(-400,-270)
tB.pendown()

colors=["white","black"]
seg=40
seglen=50
line.hideturtle()
line.pensize(10)
line.up()
line.goto(400,500)
line.down()
line.setheading(270)
for i in range(seg):
    line.pencolor(colors[i % len(colors)])
    line.forward(seg)
line.goto(400,-400)
thing = turtle.Turtle()
thing.hideturtle()
thing.penup()
thing.goto(0,250)
working=True

while working:
    for c in (tR,tP,tY,tG,tB):
        move=random.randint(1,15)
        c.fd(move)
        if c.xcor()>= 400:
            win=c.pencolor().capitalize()
            mes=f"{win} won"
            thing.color(c.pencolor())
            thing.write(mes,align="center",font=("Times new roman",67,"bold"))
            working=False
            break
turtle.exitonclick()