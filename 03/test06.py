x = int(input("금액 :"))

# x500 //= 500
# print("500원", x500)
# x //= 100
# print("100원", x)
# x //= 50
# print("50원", x)
# x //= 10
# print("10원", x)

x500 = x//500
t = x%500
x100 = t//100

t %= 100 #t = t%100
x50 = t // 50

t %= 50
x10 = t//10

print("500원 : {}  100원 : {}  50원 : {}  10원 : {}".format(x500, x100, x50, x10))