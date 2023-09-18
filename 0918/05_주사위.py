'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 주사위의 합 구하는 프로그램 --
'''

k = int(input("숫자 하나를 입력하세요 : "))

for i in range(1,7):
    for j in range(1,7):
            if i + j == k:
                  print(i, j)