side = int(input("한 변의 길이 :"))
color = input("한 변의 색깔 :")
size = int(input("한 변의 두께 :"))

import turtle
turtle.shape("turtle")

turtle.pencolor(color)
turtle.pensize(size)

for i in range(3):
    turtle.forward(side)
    turtle.left(120)

turtle.done()