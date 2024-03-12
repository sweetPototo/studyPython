name = input("이름:")
year = int(input("출생연도:"))

age = 2023 - year + 1

print("이름 :", name , "나이 :", age)
print("이름 : %s 나이 : %d" % (name, age))
print("이름 : {} 나이 : {}".format(name, age))