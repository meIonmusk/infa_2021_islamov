import turtle

turtle.shape('turtle')
turtle.speed(0)


def star(n):
    a = 100
    for i in range(n):
        turtle.forward(a)
        turtle.right(180 - 180/n)


turtle.shape('turtle')
turtle.penup()
turtle.backward(200)
turtle.pendown()
star(5)
turtle.penup()
turtle.forward(250)
turtle.pendown()
star(11)
