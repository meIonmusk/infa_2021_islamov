import turtle

turtle.shape('turtle')
turtle.speed(0)

a = 10
n = 40
for i in range(n):
    turtle.forward((i + 1) * a)
    turtle.left(90)