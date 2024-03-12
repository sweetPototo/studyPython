#콤마를 사용하여 파이썬 프로그래밍 출력
print("파이썬","프로그래밍")

# print("파이썬"+"프로그래밍",sep=" ")

a = "파이썬"
b = "프로그래밍"
# print(a + b, sep=" ")
print(a, b)

print("파이썬" + " " + "프로그래밍")

print(a + " " + b)



#3, 10, 0 정수 출력
#쉼표를 이용하여 출력하는 방법
print(3, -10, 0)
a=3
b=-10
c=0
print(a, b, c)
print("3", "-10", "0")

#형식지정자(서식지정자)를 사용하여 출력하는 방법
# 정수 : %d  실수 : %f  문자열 : %s
print("%d %d %d" % (3, -10, 0))  #순서대로 %d에 들어감
print("%d %d %d" % (a, b, c))

#포맷함수를 이용하여 출력하는 방법
print("{} {} {}".format(3, -10, 0)) #포맷함수 안의 인수들이 각각의 대괄호 안으로 순서대로 들어감
print("{} {} {}".format(a, b, c))



#3.14 -10.01 0.1 실수 출력
#쉼표를 이용해서 출력하는 방법
print(3.14, -10.01, 0.1)
a=3.14 #=은 대입연산자 왼쪽에 있는 데이터를 오른쪽으로 대입(?)
b=-10.01
c=0.1
print(a, b, c)

print("%.2f %.2f %.1f" % (3.14, -10.01, 0.1))  #%f는 소숫점 6재짜기까지 나타냄 %와 f사이에 .(원하는 소수점자리수) 지정 가능
print("%.2f %.2f %.1f" % (a, b, c))

print("{} {} {}".format(3.14, -10.01, 0.1))
print("{} {} {}".format(a, b, c))




#정수 3, -10, 0을 +연산자를 이요하여 -7의 값이 나오도록 출력
print(3+-10+0)
a=3
b=-10
c=0
print(a+b+c)
print("%d" % (3-10+0))
print("{}".format(3-10+0))
print("%d" % (a+b+c))
print("{}".format(a+b+c))




#정수 3과 실수 10.01 출력
print(3, 10.01)  #변수를 지정하지 않으면 컴퓨터가 알아서 버퍼메모리에 저장하여 출력함
a=3              #변수를 지정하면 a라는 저장공간이 메모리에 생기게 됨
b=10.01
print(a, b)
print("%d %.2f" % (3, 10.01)) #형식지정자를 사용하면 형식지정자의 형식 그대로 출력됨
print("%d %.2f" % (a, b))
print("{} {}".format(3, 10.01))
print("{} {}".format(a, b))




#1~10 중 홀수 출력하기
print(1, 3, 5, 7, 9)

#1~100까지의 모든 수 출력하기
# print(1)
# for i in range(100):
#     a=1
#     b=print(a+1)

for i in range(1, 101):
    print(i, end=" ")
print("")

for i in range(100):  #앞에 0이 생략되어 있음. 숫자를 지정해주면 그 숫자부터 시작함
    print(i+1, end=" ")
print("")




# A 4번 반복해서 출력하기
print("A"*4)
print("A"+"A"+"A"+"A")
print("A", "A", "A", "A", sep="")
print("%s%s%s%s" % ("A", "A", "A", "A"))
print("{}{}{}{}".format("A", "A", "A", "A"))
# for i in range(4):
#     i="A"
#     print(i, end=" ", sep="")
print("")
for i in range(4):
    print("A", end="")
print("")  #end로 인한 줄바꾸지않음을 끊어주는 용도




#학번+이름을 문자데이터로 작성한 후 3회 반복
print(("221078"+"최지영")*3)

for i in range(3):
    print("221078"+"최지영", end="")
print("")






# "#"3번, "*" 4번 반복한 결과를 2번 반복하기 (중첩for문)
# for w in range(2):
#     for i in range(3):
#     print('#', end="")
#     for a in range(4):
#     print("*", end="")

for j in range(2):
    for i in range(3):   #tab키를 누르면 한번에 다른 함수 안에 넣을 수 있음
        print("#", end="")
    for i in range(4):
        print("*", end="")




