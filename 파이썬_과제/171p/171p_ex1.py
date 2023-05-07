'''
2023.05.07
박수연
10개의 숫자를 입력받아 0보다 큰 수에 대해서만 전체 합과 평균을 출력하는 프로그램

# 문제분석
    변수 - 입력 받는 숫자 (num), 전체 합 (hap), 10개의 숫자를 입력받기 위한 변수 (count)
    조건 - 10개의 숫자 입력받기 (반복논리 while True)
           0보다 큰 수에 대해서만 결과출력 (선택 논리 if)

# 알고리즘
    1. 변수값 초기화 (hap, count)
    2. 반복 논리
        while True:
            정수형으로 값을 입력받기
            if num>0 이면
            hap = num + hap
            count = count + 1
            if count == 10:
                무한 반복 멈추기
    
    3. 전체 합과 평균 출력
'''

hap = 0         # 변수값 초기화
count = 0       # 변수값 초기화

while True: # 무한반복 수행
    num=int(input('숫자 입력 : '))  # 입력받는 값은 정수형
    if num>0:
        hap = hap+num   # 전체 합
        count = count+1 # 숫자를 10번 입력받기 위한 변수
        if count==10:
            break   # 숫자를 10번 입력받으면 반복 벗어남

print('입력받은 숫자의 전체 합은 {}이고 평균은 {}'.format(hap,hap/count))