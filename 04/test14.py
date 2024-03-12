m = int(input("구입 음원 :"))

sum = m * 400
half = sum * 0.3

print("구입 음악 개수 :", m)
print("총 가격 : %d원" % (sum))
print("할인금액 : %d원" % (half))
print("총 구입 가격 : %d원" % (sum - half))