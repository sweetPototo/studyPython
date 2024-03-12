a = input("문자열 :")

print(a.replace("o", "$"))


for i in range(len(a)):
    if a[i] =="o":  #다른가요?
        print("$", end="")
    else:   #그렇지 않다면
        print(a[i], end="")
