import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.shape('turtle')


def polygon(n, a):
    for j in range(n):
        t.forward(a)
        t.left(360 / n)


r = 20
t.left(180)
for i in range(3, 12):
    t.right(90 * (i - 2) / i)
    polygon(i, 2 * (i - 1.7) * r * math.sin(math.pi / i))
    t.left(90 * (i - 2) / i)
    t.penup()
    t.backward(r)
    t.pendown()
