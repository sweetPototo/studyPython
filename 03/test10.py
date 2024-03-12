# sco1 = int(input("국어 :"))
# sco2 = int(input("영어 :"))
# sco3 = int(input("수학 :")) #변수명은 반복문으로 지정할 수 없어 컬렉션 자료형을 사용함(sco 뒤의 숫자는 문자이기 때문)


# # print("국어 :", sco1)
# # print("영어 :", sco2)
# # print("수학 :", sco3)
# # print("총점 :", sco1 + sco2 + sco3)
# # print("평균 :", (sco1 + sco2 + sco3)/3) #변수명이 반복하는 것은 반복문으로 지정할 수 없다  

# sum = sco1 + sco2 + sco3
# avg = sum/3
# print("합 : %d  평균 : %.2f" % (sum, avg))

#컬렉현 자료형 : 저장곤간 1개, but 여러개를 저장 가능

a = [78, 88, 93]  #리스트(대괄호 사용) a라는 저장공간에 78, 88, 93이라는 각각의 값을 저장하고, 출력해낼 수 있음  []안의 숫자는 인덱스라고 부름
print(a)
print(a[0]) #첫번째 칸인 78점이 출력(0부터 시작, 0은 숫자임->반복문 돌릴 때 사용하기 위해서)

sum = a[0] + a[1] + a[2]
print(sum)
sum = 0

for i in range(3):
    sum = sum + a[i] #sum += a[i]  누적합

print(sum)