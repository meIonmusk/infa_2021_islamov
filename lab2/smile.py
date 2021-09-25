import turtle

turtle.speed(0)
turtle.shape('turtle')


def circle(r):
    n = 60
    for i in range(n):
        turtle.forward(r)
        turtle.left(360 / n)


def half_circle(r):
    n = 30
    for i in range(n):
        turtle.forward(r)
        turtle.right(180 / n)


turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
circle(15)
turtle.end_fill()
turtle.forward(15)
turtle.left(90)
turtle.forward(230)
turtle.left(90)
turtle.forward(50)
turtle.begin_fill()
turtle.color('blue')
circle(2)
turtle.end_fill()
turtle.penup()
turtle.backward(100)
turtle.pendown()
turtle.begin_fill()
circle(2)
turtle.end_fill()
turtle.penup()
turtle.forward(50)
turtle.left(90)
turtle.forward(60)
turtle.width(12)
turtle.pendown()
turtle.color('black')
turtle.forward(50)
turtle.penup()
turtle.left(90)
turtle.forward(65)
turtle.color('red')
turtle.right(90)
turtle.pendown()
half_circle(7)
