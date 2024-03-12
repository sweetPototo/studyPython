a = []
b = ['국어', '영어', '수학']

# for i in range(3):
#     a.append(int(input(b[i]+"점수:")))

# print(a)

sum = 0
# for i in range(3):
#     sum += a[i]

# c = sum/3

# print("총점 :", sum)
# print("평균 : %.1f" % c)


for i in range(3):
    tmp = int(input(b[i] + "점수입력 :"))
    a.append(tmp)
    sum += a[i]

