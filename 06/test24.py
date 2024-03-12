#3과 5의 배수의 합 구하기

# a = []
# sum = 0
# for i in range(19):
#     sum += 1
#     a.append(sum)

# print(a)

# set3 = {}
# set5 = {}
# for i in range(18):
#     if a[i] % 3 == 0:
#         set3.update(a)
#     if a[i] % 5 == 0:
#         set5.update(a)
# print(set3)
# print(set5)


s = 0
for num in range(1000):
    if num % 3 ==0 or num % 5 == 0:
        s += num
print(s)