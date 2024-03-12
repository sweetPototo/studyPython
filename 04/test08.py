a = input("문자열 :")
sum = 0
count = len(a)

for i in range(len(a)):
    sum -= 1
    print(a[sum], end="")
print("")

for i in range(count):
    print(a[count-(i+1)], end="")