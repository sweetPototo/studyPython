import turtle
turtle.shape("turtle")

turtle.right(90)
for i in range(3):
    turtle.goto(50*i,0)
    turtle.down()
    turtle.forward(100)
    turtle.up()


turtle.done()
