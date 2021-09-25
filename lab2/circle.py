import turtle

turtle.shape('turtle')
turtle.speed(0)

n = 50
for i in range(n):
    turtle.forward(15)
    turtle.left(360 / n)
