'''
신라대학교 202395016 컴퓨터공학부 박수연

# 문제정의
    5과목의 성적을 입력받아 각 과목의 점수, 총점, 평균을 출력하는 프로그램, 입력된 각 과목의 성적이 0부터 100 사이의 점수가 아닌 경우에는
    '유효한 성적이 아닙니다' 출력

# 문제분석
    변수 - 입력받을 과목 점수 (sub), 횟수 초깃값 (i), 총점을 저장할 변수 (total)

# 알고리즘
    1. 변수 지정하기
        횟수 변수 1로 초기화
        total 변수 0으로 초기화

    2. 반복문 (while) - i가 5보다 작거나 같을때까지 반복
        i번째 성적 입력받기
        2-1. 조건문(if) - 입력받은 sub 변수가 0보다 크거나 같고 100보다 작거나 같다면
            i번째 성적 출력하기
            total 변수에 총점 저장
            횟수 1씩 증가시키기
        그렇지 않으면
            유효한 성적 아닙니다 출력   
        

    3. 총점과 평균 출력하기
'''

i=1         # 횟수 변수 1로 초기화
total=0     # 총점 저장할 변수 0으로 초기화

while i<=5:                                             # i가 5보다 작거나 같을때까지 반복
    sub=int(input("{}번째 성적 입력 : ".format(i)))      # 정수로 입력받기
    if 0<=sub<=100:                                     # 입력받은 성적 점수가 0보다 크거나 같고 100보다 작거나 같다면
        print("{}번째 성적 : {} ".format(i,sub))         # 성적 출력하기
        total=total+sub                                 # 총점 저장
        i=i+1                                           # 횟수 1씩 증가   
    else:     
        print("유효한 성적이 아닙니다")

print("총점 : ", total)
print("평균 : ", total/i)