a = "123456789"
# int(a)
# print(type(a))

# for i in range(len(a)):
#     sum = 0
#     sum = a[i]
    
#     print(sum+sum)

s = 0
for i in range(len(a)):
    s += int(a[i])
print("합 :", s)