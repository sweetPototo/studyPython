#세트는 합집합, 교집합, 차집합을 출력
#& : 교집합   |:합집합   - : 차집합

A = {10,20,30}
B = {20,40}
print(A&B)
print(A.intersection(B))

print(A|B)
print(A.union(B))

print(A-B)
print(A.difference(B))

print(B-A)
print(B.difference(A))

a = {100,200,300}

a.add(400)
print(a)

a.update([500,600])  #[]안의 값 아님. 데이터를 묶어서 처리한다는 뜻
print(a)

a.remove(400)
print(a)