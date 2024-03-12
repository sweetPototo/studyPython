import random

a = ["red", "blue", "green", "purple"]

print(random.choice(a)) #컬렉션 자료형에 있는 값중 하나를 추출해주는 함수
print(random.randint(1, 3)) #1~3중 무작위로 추출
print(random.randrange(1, 3)) #1~2까지의 숫자 중 무작위로 추출
print(random.shuffle(a)) #리스트의 값을 무작위로 섞음
print(a)
print(random.random()) #파이썬에서 최대값으로 출력할 수 있는 소수점 15자리까지 0~1사이의 실수값 무작위로 출력
