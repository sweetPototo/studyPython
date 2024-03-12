a = {"김밥":2000, "라면":3000, "돈까스":5000}
print(a)
a["라면"]=3500
print(a)

print(a.keys()) #키값만 출력
print(a.values()) #발루값만 출력
print(a.items()) #키값, 발루값을 튜플로 출력

#형변환 함수
print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))

print(tuple(a.keys()))
print(set(a.keys()))