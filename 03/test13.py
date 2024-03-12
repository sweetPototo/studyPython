radius = int(input("원의 반지름 :"))

a = radius **2 * 3.14
b = radius * 2 * 3.14

print("원의 넓이 :", a, "원의 둘레 :", b)
print("원의 넓이 : %.2f 원의 둘레 : %.2f" % (a, b))
print("원의 넓이 : {} 원의 둘레 : {}".format(a, b))
