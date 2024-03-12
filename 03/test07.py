a = int(input("정수1 :"))
b = int(input("정수2 :"))

print("%.17f" % (a / b))
print("%d / %d = %f" % (a, b, a/b))  #정수를 정수로 나눠도 실수값이 나옴
print(a // b)
print(a % b)
print("%d %% %d = %d" % (a, b, a%b))