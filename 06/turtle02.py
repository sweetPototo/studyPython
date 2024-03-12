
import random


a = int(input("길이 :"))
c = ["red", "yellow", "blue", "green", "purple"]
l = [1, 3, 5, 2, 8]

import turtle
turtle.shape("turtle")

for i in range(5):
    r = random.random() #0.0001~0.9999
    g = random.random()
    b = random.random()
    turtle.pencolor([r, g, b]) #하나의 색으로 인식시키기위해 리스트 또는 튜플로 입력 r, g, b 3개의 채널이 묶여서 하나의 색을 만든다는 뜻
    turtle.pensize(random.randint(1,10))
    turtle.forward(a/l[i])
    turtle.right(45)

turtle.done()