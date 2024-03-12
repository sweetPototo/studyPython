#사용자로부터 학번과 이름을 입력받아 출력받기
stud_num = input("학번 : ")
name = input("이름 : ")

print("학번:", stud_num, "이름:", name)
print("학번: %s  이름: %s" % (stud_num, name))
print("학번: {} 이름: {}".format(stud_num, name))