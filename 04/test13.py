# score = [0, 0, 0,]
# sum = 0

# for i in range(3):
#     print(score[i]+score[i+1]+score[i+2])

score = [0, 0, 0]
for i in range(3):
    score[i] = int(input("점수 :"))

print(score)

sum = 0
avg = 0

for i in range(3):
    sum += score[i]
print(sum)

for i in range(3):
    avg = sum/3
print(avg)
