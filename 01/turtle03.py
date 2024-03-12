import turtle #터틀을 모듈이라고 부름  터틀은 박스고, 박스 안에 함수를 담는 개념
turtle.shape("turtle")

# turtle.right(90)
# turtle.forward(100)  한꺼번에 주석처리  드래그 후 커느롤 슬래쉬
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

for i in range(4):  #for ~하는 동안에 i 임의의 변수
    turtle.forward(100)  #들여쓰기는 반복문의 영역
    turtle.right(90)

turtle.done()
