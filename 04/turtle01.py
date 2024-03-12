

import turtle
import random

turtle.shape("turtle")

for i in range(5):
    x = int(input("x 좌표 :"))
    y = int(input("y 좌표 :"))
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.stamp()

turtle.done()