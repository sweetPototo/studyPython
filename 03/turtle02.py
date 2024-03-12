length = int(input("길이 :"))

import turtle
turtle.shape("turtle")

turtle.pencolor("red")
turtle.forward(length*(2**0))
turtle.right(45)

turtle.pencolor("yellow")
turtle.forward(length*(2**1))
turtle.right(45)

turtle.pencolor("blue")
turtle.forward(length*(2**2))
turtle.right(45)

turtle.pencolor("green")
turtle.forward(length*(2**3))
turtle.right(45)

turtle.pencolor("purple")
turtle.forward(length*(2**4))
turtle.right(45)




# a = ["red", "yellow", "blue", "green", "purple"]

# for i in range(5):
#     turtle.pencolor(a[i])
#     turtle.forward(length*(2**i))
#     turtle.right(45)

turtle.done()