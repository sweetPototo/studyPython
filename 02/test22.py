a = int(input("길이 :"))

import turtle
turtle.shape("turtle")

# turtle.delay(50)

for i in range(6):
    turtle.forward(a)
    turtle.left(30)
    turtle.backward(a)
    turtle.left(30)

turtle.up()
turtle.goto(300,0)
turtle.down()

for i in range(4):
    turtle.forward(a)
    turtle.left(45)
    turtle.backward(a)
    turtle.left(45)

turtle.up()
turtle.goto(-300,0)
turtle.down()

for i in range(3):
    turtle.forward(a)
    turtle.left(36)
    turtle.backward(a)
    turtle.left(36)



turtle.done()