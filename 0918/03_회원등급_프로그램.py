'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 회원등급 프로그램 --
'''
def solution():
    global price, grade
    if grade == "S":
        price = price * 0.95
    elif grade == "G":
        price = price * 0.9
    elif grade == "V":
        price = price * 0.85
    else:
        print("회원등급이 올바르지 않습니다.")

price = int(input("가격을 입력하세요 : "))   # 가격
grade = input("등급을 입력하세요(S, G, V): ")   # 등급

solution()
print("고객님의 등급은 {}이며, 등급할인 서비스 적용으로 {}원 입니다.".format(grade, int(price)))