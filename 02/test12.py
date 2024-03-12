s="#"

for i in range(5):     #Range 안에 있는 숫자 0~4받는 동안
    print(s, end="")   #s를 출력하라
print("")

for i in range(5):
    print("%s" % s, end="")
print("")

for i in range(5):
    print("{}".format(s), end="")