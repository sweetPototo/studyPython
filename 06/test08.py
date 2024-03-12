name = {100:'황복동', 200:'황나연', 300:'황채연'}
print(name[100])

print(name.get(100))
print(name.get(400, "없습니다")) #없습니다 출력
print(name.get(200, "없습니다"))