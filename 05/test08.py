a = []

for i in range(4):
    a.append(0)

for i in range(4):
    a[i] = int(input(str(i+1)+"번째정수입력 :"))

sum = 0
for i in range(4):
    sum += a[i]
print("합 :", sum)

#=========================================================

a = []
s = 0
for i in range(4):
    tmp = int(input(str(i+1)+"번째 정수입력 :"))
    a.append(tmp)  #append를 사용하면 리스트에 0을 추가해주는 작업을 안해줘도 됨
    s += a[i]

print(a)

