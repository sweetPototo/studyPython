radius = int(input("반지름 :"))
color = input("색 :")
size = int(input("두께 :"))

import turtle
turtle.shape("turtle")

turtle.pencolor(color)
turtle.pensize(size)
turtle.circle(radius)
for i in range(3,7):
    turtle.circle(radius, steps=i)

turtle.done()