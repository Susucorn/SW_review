'''
신라대학교 202395016 컴퓨터공학부 박수연

# 문제정의
    사용자로부터 입력받은 숫자에 해당하는 구구단을 출력하는 프로그램

# 문제분석
    변수 - 입력받을 숫자 (dan)

# 알고리즘
    1. 변수 지정하기
        정수로 입력받기
    2. 반복문 (for) - 범위는 1부터 9까지
        구구단 출력
'''

dan=int(input("출력을 원하는 단을 입력하세요 : "))      # 정수로 입력받기
print("==========", dan, "단============")

for i in range(1,10):                                 # 1부터 9까지 반복
    print("{} * {} = {}".format(dan, i, dan*i))       # 구구단 출력