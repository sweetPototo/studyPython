tt1 = 10,20,30,40
tt2 = 'A', 'B'

print(tt1+tt2)
print(tt1*3)
print(tt2*3)

a = 10,20,30
b = ((10,20,30),
     (40,50,60),
     (70,80,90))

print(a[0])
print(b[0][0])

for i in range(3):
    print(a[i], end=" ")
print("")

for i in range(3):
    print(b[0][i], end=" ")
for i in range(3):
    print(b[1][i], end=" ")
for i in range(3):
    print(b[2][i], end=" ")
print("")

