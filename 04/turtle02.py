import turtle
import random

turtle.shape("turtle")
turtle.speed(3)

for i in range(30):
    x = random.randint(-300,301)
    y = random.randint(-300,301)
    turtle.up()
    turtle.goto(x, y)
    turtle.stamp()

turtle.done()