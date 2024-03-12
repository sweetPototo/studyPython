import turtle
turtle.shape("turtle")

turtle.pencolor("red")
turtle.circle(100)

turtle.pencolor("blue")
# for i in range(4):
#     turtle.circle(100, steps = i + 3)

for i in range(3,7):
    turtle.circle(100, steps = i)

turtle.done()
