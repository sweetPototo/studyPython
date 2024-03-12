#10~15 숫자개수 구하기
num = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for i in range(1,1001):
    for j in str(i): #i값이 10이라면 j에 1 0 이 들어감
        num[int(j)] = num[int(j)] + 1

print(num)