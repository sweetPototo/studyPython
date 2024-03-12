# 1부터 100까지의 숫자 불러오기
for i in range(100):
    print(i+1, end=" ")
print("")

for i in range(1, 101):  #range 안의 숫자들을 i 안에 넣어서 range안의 범위만큼 반복해라
    print(i, end=" ")
print("")




# 1부터 100까지의 수 중 홀수 불러오기
for i in range(1, 101):
    if i % 2 == 1: #입력받은 i값을 2로 나누었을때(%2) 1과 똑같은가?(==1) -> 홀수인가요?
        print(i, end=" ")  #if함수로 조건을 건 결과값만 출력받을 것이기 때문에 if문 안에서 print함수 쓰기
print("")




# 1부터 100까지의 수 중 짝수 불러오기
for i in range(1, 101):
    if i % 2 ==0:
        print(i, end=" ")
print("")