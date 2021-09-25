import turtle

turtle.shape('turtle')
turtle.speed(0)

a = 10
for i in range(10):
    for j in range(4):
        turtle.forward((i+1) * a * 2)
        turtle.left(90)
    turtle.penup()
    turtle.left(45)
    turtle.backward((2*a*a) ** 0.5)
    turtle.right(45)
    turtle.pendown()
