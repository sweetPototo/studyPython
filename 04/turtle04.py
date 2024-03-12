import turtle
import random

turtle.shape("turtle")
turtle.speed(10)
a = ["red", "blue", "green", "purple", "orange", "pink", "skyblue", "black", "gray", "yellow"]


for i in range(30):
    turtle.up()
    turtle.goto(random.randint(-400,401), random.randint(-400,401))
    turtle.pensize(random.randint(1, 10))
    turtle.pencolor(random.choice(a))
    turtle.down()
    turtle.circle(random.randint(10, 200), steps=random.randint(3,7))

turtle.done()