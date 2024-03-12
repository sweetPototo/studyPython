import turtle
import random

turtle.shape("turtle")
turtle.speed(10)


for i in range(30):
    turtle.up()
    turtle.goto(random.randint(-400,401), random.randint(-400,401))
    turtle.down()
    turtle.circle(random.randint(10, 200))

turtle.done()