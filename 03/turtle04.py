a = int(input("길이 :"))
b = int(input("간격 :"))

import turtle
turtle.shape("turtle")


for i in range(3):
    turtle.goto(0,-b*i)
    turtle.down()
    turtle.forward(a)
    turtle.up()

turtle.done()