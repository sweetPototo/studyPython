a = int(input("길이 :"))
b = [2,1,3,6,3,5]
c = ["red", "blue", "green", "purple", "orange", "pink"]
d = [0,100,40,30,70,10]
y = 0

import turtle
turtle.shape("turtle")

for i in range(6):
    y += d[i]
    turtle.goto(0, y)
    turtle.pensize(b[i])
    turtle.pencolor(c[i])
    turtle.down()
    turtle.forward(a)
    turtle.up()

turtle.done()

