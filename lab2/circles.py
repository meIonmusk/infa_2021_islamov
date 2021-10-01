import turtle

turtle.shape('turtle')
turtle.speed(0)


def circle_left(r):
    k = 100
    for j in range(k):
        turtle.forward(r)
        turtle.left(360 / k)


def circle_right(r):
    k = 100
    for j in range(k):
        turtle.forward(r)
        turtle.right(360 / k)


n = 4
a = 5
for i in range(n):
    circle_left(a)
    circle_right(a)
    turtle.left(180 / n)
