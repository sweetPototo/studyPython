a = []

for i in range(3):
    a.append(0)
print(a)

for i in range(3):
    a.pop()
print(a)

for i in range(3):
    a.insert(i, 0)
print(a)

for i in range(3):
    a.remove(0)
print(a)

#리스트 표현식
d = [0 for i in range(3)]
print(d)