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



line.hideturtle()
line.color("white")
line.pensize(10)
line.up()
line.goto(400,400)
line.down()
line.goto(400,-400)

tR.speed(random.randint(1,5));tP.speed(random.randint(1,5));tY.speed(random.randint(1,5));tG.speed(random.randint(1,5));tB.speed(random.randint(1,5))
tR.goto(-200,370);tP.goto(-200,210);tY.goto(-200,50);tG.goto(-200,-120);tB.goto(-200,-270)
tR.speed(random.randint(1,5))
tP.speed(random.randint(1,5))
tY.speed(random.randint(1,5))
tG.speed(random.randint(1,5))
tB.speed(random.randint(1,5))
tR.goto(0,370)
tP.goto(0,210)
tY.goto(0,50)
tG.goto(0,-120)
tB.goto(0,-270)
tR.speed(random.randint(1,5))
tP.speed(random.randint(1,5))
tY.speed(random.randint(1,5))
tG.speed(random.randint(1,5))
tB.speed(random.randint(1,5))
tR.goto(200,370)
tP.goto(200,210)
tY.goto(200,50)
tB.goto(200,-270)
tG.goto(200,-120)
tR.speed(random.randint(1,5))
tP.speed(random.randint(1,5))
tY.speed(random.randint(1,5))
tG.speed(random.randint(1,5))
tB.speed(random.randint(1,5))
tR.goto(400,370)
tP.goto(400,210)
tY.goto(400,50)
tG.goto(400,-120)
tB.goto(400,-270)
turtle.exitonclick()