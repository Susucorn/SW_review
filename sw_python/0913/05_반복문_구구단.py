'''
    신라대학교 202395016 컴퓨터공학부 박수연
'''

# 입력받은 수의 구구단
n = int(input("숫자를 입력하세요 : "))

for i in range(1,10):
    value = n * i
    print("{} * {} = {}".format(n, i, value))