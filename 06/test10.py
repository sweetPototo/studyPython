tel = {'홍길동':'010-2345-6789',
       '김말자':'010-3456-1234',
       '박문순':'010-5791-2654'}
print(list(tel.keys()))

a = input("이름 :")
print(tel.get(a, "없습니다."))