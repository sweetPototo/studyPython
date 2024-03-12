a = int(input("길이 :"))
b = int(input("두께 :"))
c = ["red", "blue", "purple"]

import turtle
turtle.shape("turtle")

turtle.pensize(b)

for i in range(3):
    turtle.pencolor(c[i])
    turtle.forward(a)
    turtle.left(120)

turtle.done()