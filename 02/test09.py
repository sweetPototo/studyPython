name = input("이름 :")
year = int(input("출생년도 :"))

print("이름 :", name, "출생년도 :", year)
print("이름 : %s 출생년도 : %d" % (name, year))
print("이름 : {} 출생년도 : {}".format(name, year))