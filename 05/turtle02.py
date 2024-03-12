a = int(input("길이 :"))
b = [2,1,3,6,3]
c = ["red", "green", "blue", "purple", "orange"]

import turtle
turtle.shape("turtle")

for i in range(5):
    turtle.pensize(b[i])
    turtle.pencolor(c[i])
    turtle.forward(a)
    turtle.right(144)

turtle.done()