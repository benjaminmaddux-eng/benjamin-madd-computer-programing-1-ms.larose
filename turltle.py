import turtle
window = turtle.Screen()
window.bgcolor("black")
colors=["white","cyan","purple"]
t = turtle.Turtle()
t.speed(40)
t.pensize(2)

t.right(45)

for i in range(800):
    t.color("cyan","white","blue")
    t.circle(600) 
    if i < 200:
        t.left(50)
        t.right(-50000)
turtle.done()