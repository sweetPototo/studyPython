top = int(input("윗변 :"))
bottom = int(input("밑변 :"))
height = int(input("높이 :"))

fill = (top + bottom ) * height / 2

print("사다리꼴의 넓이 :", fill)
print("사다리꼴의 넓이 : %.1f" % (fill))
print("사다리꼴의 넓이 : {}".format(fill))