a = []
b = ['닭', '토끼', '돼지']
l = [2, 4, 4]
sum = 0

for i in range(3):
    tmp = int(input(b[i] + ":"))
    a.append(tmp)
    sum += a[i]*l[i]

print("다리 합계 :", sum)

