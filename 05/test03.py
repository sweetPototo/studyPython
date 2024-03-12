# a1 = int(input("정수1:"))
# a2 = int(input("정수2:"))
# a3 = int(input("정수3:"))
# a4 = int(input("정수4:"))

# print(a1 + a2 + a3 + a4)

a = [0, 0, 0, 0]

for i in range(len(a)):
    a[i] = int(input("정수:"))

sum = 0
for i in range(len(a)):
    sum += a[i] #sum = sum + a[i]
print(sum)