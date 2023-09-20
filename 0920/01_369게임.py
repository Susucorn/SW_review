'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 369 게임 프로그램 --
'''
i = 1   # 변수 초기화
num = int(input("숫자 하나를 입력하세요 : "))   # 정수로 입력받기
print()
print(f"입력하신 숫자 {num}으로 게임을 시작합니다.")
print(f"{num}의 배수일때 박수를 치세요.")
print()            

while i <= 100:
    if i % num == 0:
        print("박수", end=" ")
    else:
        print(i, end =" ")
    i+=1
'''
# for 문으로 반복
for i in range(1,101):
    if i % num == 0:
        print("박수", end=" ")
    else:
        print(i, end =" ")
'''