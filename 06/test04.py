# a = []
# a1 = []

# sum = 0

# for j in range(3):
#     for i in range(4):
#         sum += 1
#         a1.append(sum)
#     a.append(a1)


# print(a)




# b = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12]]

# print(b)

# for i in range(3):
#     for j in range(4):
#         print(b[i][j], end=" ")
#     print("")

list1 = []
value = 1

for i in range(3): #행
    tmp = []
    for j in range(4):
        tmp.append(value)
        value += 1
    list1.append(tmp)
print(list1)

for i in range(3):
    for j in range(4):
        print("%3d" %list1[i][j], end=" ")  #%3d 3칸씩 띄어쓰기한다
    print("")

#이차원리스트는 항상 행 열 순으로 코드작성

