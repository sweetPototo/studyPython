s=0
for i in range(10,101):
    for j in str(i): #문자열로 바꾼 i값이 j에 들어감
        print(j, end=" ")
        s += int(j)
    print("")

print("합 :", s)
