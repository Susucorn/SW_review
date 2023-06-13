'''
신라대학교 202395016 컴퓨터공학부 박수연

# 문제정의
    1부터 100사이의 수 중에서 2의 배수이면서 3의 배수가 아닌 수를 모두 출력하는 프로그램

# 문제분석
    변수 - 횟수 초깃값 (i)

# 알고리즘
    1. 변수 초기화
    2. 반복문 (while) - i가 100보다 작거나 같을때까지 반복
        2-1. 조건문 (if) - i를 2로 나눈 나머지가 0이고, i를 3으로 나눈 나머지가 0이 아니라면
        2의 배수이면서 3의 배수가 아닌 숫자 출력
        횟수 1씩 증가시키기
'''

i=1     # 변수 초기화
print("1부터 100사이의 숫자 중에서 2의 배수이면서 3의 배수가 아닌 숫자는 : ")

while i <= 100:             # i가 100보다 작거나 같을때까지 반복
    if i%2==0 and i%3!=0:   # i를 2로 나눈 나머지가 0이고, i를 3으로 나눈 나머지가 0이 아니라면
        print(i)            # 2의 배수이면서 3의 배수가 아닌 숫자 출력
    i=i+1                   # ** 들여쓰기 유무 중요 **

