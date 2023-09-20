'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 두 수 중에 큰 수 출력하는 프로그램 --
'''
num1 = int(input("첫번째 정수를 입력하세요 : "))
num2 = int(input("두번째 정수를 입력하세요 : "))

if num1 > num2:
    print(f"두 정수 중에 큰 수는 {num1}입니다.")
elif num1 < num2:
    print(f"두 정수 중에 큰 수는 {num2}입니다.")
else:
    print("두 정수는 같은 수 입니다.")