a = []
for i in range(100):
    a.append(2*i)
print(a)

b = []
a.reverse()
b.append(a)
print(b)

#=====================

aa = []
bb = []
value = 0
for i in range(100):
    aa.append(value)
    value += 2
print(aa)
print(aa.index(198))

for i in range(100):
    bb.append(aa[99-i])
print(bb)