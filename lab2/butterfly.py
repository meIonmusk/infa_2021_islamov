import turtle

turtle.shape('turtle')
turtle.speed(0)


def circle_left(r):
    k = 40
    for j in range(k):
        turtle.forward(r)
        turtle.left(360 / k)


def circle_right(r):
    k = 40
    for j in range(k):
        turtle.forward(r)
        turtle.right(360 / k)


n = 9
turtle.left(90)
for i in range(n):
    circle_left(8 + 2*i)
    circle_right(8 + 2*i)
