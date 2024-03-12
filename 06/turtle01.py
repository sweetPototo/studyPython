color = ("red", "yellow", "blue", "green", "purple")
size = (2,1,6,3,5)
len = (1,3,5,2,8)
sum = 0
a = int(input("길이 :"))

import turtle
turtle.shape("turtle")

for i in range(5):
    turtle.pencolor(color[i])
    turtle.pensize(size[i])
    turtle.forward(a*len[i])
    turtle.right(45)

turtle.done()