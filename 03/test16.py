sec = int(input("초 :"))

min = sec//60
sec2 = sec%60


print(sec, "초 =", min, "분", sec2, "초")
print("%d초 = %d분 %d초" % (sec, min, sec2))