length = int(input("길이 :"))
line = str(input("색 :"))
pen = int(input("두께 :"))

import turtle
turtle.shape("turtle")

turtle.pencolor(line)
turtle.pensize(pen)
turtle.forward(length)

turtle.done()