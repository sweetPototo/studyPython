#중첩 for문
b = ((10,20,30),
     (40,50,60),
     (70,80,90))

for i in range(3):
    for j in range(3):
        print(b[i][j], end=" ")
    print("") #줄바꿈