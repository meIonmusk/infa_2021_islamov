import turtle

turtle.speed(0)
turtle.shape('turtle')

n = 12
a = 100
for i in range(n):
    turtle.forward(a)
    turtle.stamp()
    turtle.backward(a)
    turtle.left(360 / n)
