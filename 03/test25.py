#1부터 100까지의 홀수 합
s=0

for i in range(1,101):
    if i % 2 == 1: #관계연산자에 의해 true or false값이 나옴
        s += i #s = s + i
print("홀수 합:", s)