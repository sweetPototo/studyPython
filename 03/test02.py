#500원짜리와 100원짜리 개수 구하기

x = int(input(("정수 :")))

x500 = x//500
x100 = (x %500)//100

print("500원 :", x500)
print("100원 :", x100)

print("500원 {}개  100원 {}개".format(x500, x100))