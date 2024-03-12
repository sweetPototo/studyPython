minute = int(input("분 :"))

second = 60*minute

print(second, "초", sep="")
print("%d초" % second)
print("{}초".format(second))