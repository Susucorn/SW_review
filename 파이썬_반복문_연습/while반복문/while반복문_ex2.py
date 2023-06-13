'''
신라대학교 202395016 컴퓨터공학부 박수연

# 문제정의
    두 개의 숫자를 입력받아 두 수 사이의 모든 정수값을 더하여 출력하는 프로그램

# 문제분석
    변수 - 입력받을 숫자 2개 (num1, num2), 합을 저장할 변수 (hap), 값을 임시 저장할 변수 (temp)

# 알고리즘
    1. 변수 지정하기
        입력받는 변수는 정수형
        합계 변수 0으로 초기화
    2. 조건문 (if) - num1이 num2보다 크다면
        temp 변수에 num1값 임시로 저장
        num1에 num2 값 저장
        num2 에 임시로 저장했던 temp (num1)값 저장
    3. 반복문 (while) - num1 이 num2보다 작거나 같을때까지 반복
        hap 변수에 합계 저장
        num1변수를 1씩 증가시기키
    4. 결과 출력
'''

num1=int(input("첫 번째 숫자를 입력하세요 : "))     # 정수로 입력받기
num2=int(input("두 번째 숫자를 입력하세요 : "))     # 정수로 입력받기
hap=0                                             # 합계를 저장할 변수 0으로 초기화

if num1>num2:               # num1이 num2보다 크다면
    temp=num1               # temp 변수에 num1값을 임시 저장
    num1=num2               # num1 변수에 num2값을 저장
    num2=temp               # num2 변수에 temp(num1)값을 저장, 두 수 교환

while num1<=num2:           # num1이 num2보다 작거나 같을때까지 반복
    hap=hap+num1            # 합계 저장
    num1=num1+1             # num1을 1씩 증가시킴, 횟수 1씩 증가

print("두 수의 모든 정수값을 더한 결과는 {} 입니다. ".format(hap))