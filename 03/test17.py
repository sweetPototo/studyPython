a = float(input("1초당 움직이는 거리 :"))

b = a * 3600
c = b/1000

print("시속", b, "m/h", "시속", c, "km/h")
print("")
print("시속 %.2f m/h 시속 %.2f m/h" % (b, c))
print("")
print("시속 {} m/h 시속 {} m/h".format(b, c))
print("")