a = "python"
b = ["p", "y", "t", "h", "o", "n"]
c = ("p", "y", "t", "h", "o", "n")

print(a)

for i in range(len(b)):
    print(b[i], end ="")
print("")

for i in range(len(c)):
    print(c[i], end ="")
print("")

# print(a[0] = "K") #문자열은 한번 만들어지면 변경할 수 없음
b[0] = "K"
print(b)
c[0] = "K"
print(c)