str1 = "happy python"
str2 = "cheer up"

s1 = len(str1)
s2 = len(str2)

print("문자열의 개수의 합 :", s1 + s2)



music = "beautiful my life"

print(music[:7])
print(music[3:])
print(music[2:5])

for i in range(7):
    print(music[i], end="")
print("")

for i in range(3,len(music)):
    print(music[i], end="")
print("")

for i in range(2, 5):
    print(music[i], end="")
print("")