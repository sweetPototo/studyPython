a = int(input("반지름 :"))

import turtle
turtle.shape("turtle")

turtle.circle(a)
turtle.up()
turtle.goto(0,a*2)
turtle.down()
turtle.circle(a/2)


turtle.done()