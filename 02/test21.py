distance = int(input("길이 :"))
color = input("색깔 :")
size = int(input("두께 :"))

import turtle
turtle.shape("turtle")
turtle.fillcolor(color)
turtle.pensize(size)

for i in range(3):
    turtle.forward(distance)
    turtle.right(90)

turtle.done()