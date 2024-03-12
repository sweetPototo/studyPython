import turtle
import random

turtle.shape("turtle")
turtle.speed(5)
a = ["red", "blue", "green", "purple", "orange", "pink", "skyblue", "black", "gray", "yellow"]

turtle.up()

for i in range(30):
    turtle.goto(random.randint(-400,401), random.randint(-400,401))
    turtle.shapesize(random.randint(1,5))
    turtle.color(random.choice(a))
    turtle.right(random.randint(-360, 360))
    turtle.stamp()

turtle.done()