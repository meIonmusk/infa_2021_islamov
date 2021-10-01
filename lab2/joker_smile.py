import turtle

turtle.speed(0)
turtle.shape('turtle')
turtle.bgcolor('black')


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


def rhombus(a):
    for i in range(2):
        for j in range(3):
            turtle.forward(a)
            turtle.right(120)
        turtle.left(60)


# hair
turtle.goto(-15, -10)
turtle.color('dark green')
turtle.begin_fill()
circle(11.5)
turtle.end_fill()

turtle.goto(-15, 165)
turtle.begin_fill()
circle(4)
turtle.end_fill()

turtle.goto(-105, 42)
turtle.begin_fill()
circle(4)
turtle.end_fill()

turtle.goto(80, 42)
turtle.begin_fill()
circle(4)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(-110, -65)
circle(9)
turtle.goto(80, -65)
circle(9)
turtle.end_fill()

turtle.goto(-190, -33)
turtle.begin_fill()
circle(4)

turtle.goto(160, -33)
circle(4)
turtle.end_fill()
turtle.penup()

# head
turtle.goto(-15, -140)
turtle.pendown()
turtle.color('white')
turtle.begin_fill()
circle(14.5)
turtle.end_fill()

# makeup
turtle.goto(-30, 50)
turtle.left(180)
turtle.color('blue')
turtle.begin_fill()
rhombus(60)
turtle.end_fill()
turtle.penup()

turtle.right(120)
turtle.backward(90)
turtle.pendown()
turtle.begin_fill()
rhombus(60)
turtle.end_fill()

# eyes
turtle.goto(45, 50)
turtle.left(150)
turtle.color('gray')
turtle.begin_fill()
circle(1.7)
turtle.end_fill()
turtle.penup()

turtle.goto(-45, 50)
turtle.pendown()
turtle.begin_fill()
circle(1.7)
turtle.end_fill()
turtle.penup()

# nose
turtle.goto(15, 0)
turtle.pendown()
turtle.color('red')
turtle.begin_fill()
circle(3)
turtle.end_fill()
turtle.penup()

#  mouth
turtle.goto(53, -30)
turtle.left(180)
turtle.width(40)
turtle.pendown()
half_circle(7)
turtle.penup()
turtle.goto(53, -30)
turtle.left(180)
turtle.pendown()
turtle.color('black')
turtle.width(5)
half_circle(7)
