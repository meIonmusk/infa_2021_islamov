import turtle

turtle.shape('turtle')
turtle.speed(0)


def half_circle(r):
    k = 30
    for j in range(k):
        turtle.forward(r)
        turtle.right(180 / k)


n = 3
turtle.penup()
turtle.backward(250)
turtle.left(90)
turtle.pendown()
for i in range(5):
    half_circle(5)
    half_circle(1)
