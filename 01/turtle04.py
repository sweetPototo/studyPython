
#꼬북이를 화살로 변경, 왼 180, 앞 50 뒤 30
import turtle
turtle.shape("arrow")

# turtle.color("blue")  #화면의 모든 색을 파랑으로 바꿈(거북이까지 색을 바꾸어버림)
turtle.pencolor("blue")  #라인의 색깔만 바꿀때
turtle.pensize(3)        #펜 두께
turtle.left(180)
turtle.forward(50)
turtle.backward(30)

turtle.done()