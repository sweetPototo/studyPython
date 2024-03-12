a = "good luck"  #문자열
b = ["g", "o", "o", "d", " ", "l", "u", "c", "k"]  #컬렉션 자료형(리스트) -> 대량의 데이터를 효율적으로 관리하기 위하여 제작(keep point :  리스트의 중점 자료를 저장하고 뽑아내는 것)
c = ("g", "o", "o", "d", " ", "l", "u", "c", "k")  #컬렉션 자료형(튜플)

print(a)
print(a[0])
print(a[5])
print(b)
print(c)

print(b[0])   #인덱싱  인덱스번호로 자료를 뽑아내는 일
print(c[0])

print(a[-1])
print(b[-1])
print(c[-1])

#반복문으로 출력
for i in range(len(a)):
    print(a[i], end="")
print("")

for i in range(len(b)):
    print(b[i], end="")
print("")

for i in range(len(c)):
    print(c[i], end="")
print("")