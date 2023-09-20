'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 팩토리얼 계산하는 프로그램 --
'''
num = int(input("팩토리얼을 구할 정수를 입력하세요 : "))
fact = 1
for i in range(num, 0, -1):
    fact = fact*i

print(f"{num}!은 {fact}입니다.")