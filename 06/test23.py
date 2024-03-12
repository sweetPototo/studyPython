a = []
b = ["국어", "영어", "수학"]

sum = 0
for i in range(len(b)):
    a.append(int(input(b[i] + "점수 :")))
    sum += a[i]
print("총점 :", sum)

avg = sum/len(b)
print("평균 : %.1f" % avg)

if avg >= 80:
    print("잘함")
elif avg >=70 and avg <= 79:
    print("보통")
else:
    print("미흡")