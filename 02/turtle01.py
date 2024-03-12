import turtle
turtle.shape("turtle") #메소드=함수  터틀이라는 박스 안의 터틀을 turtle로 지정한다

turtle.pencolor("red")
turtle.fillcolor("blue")
turtle.pensize(3)

# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)

for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.done()
