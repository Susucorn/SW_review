'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- for 반복문 연습 --
'''
# for 반복문
family = ["할아버지", "할머니", "누나", "동생"]     # 변수에 리스트 선언

for i in family:                                  # 변수 안에 있는 리스트 원소를 i에 저장하여 출력함
    print("우리 가족에는 ", i, "(이)가 있습니다." )

print()

# while 반복문
family_1 = ["할아버지", "할머니", "누나", "동생"]   # 변수에 리스트 선언
i=0                                               # i를 0으로 초기화 (증감시키기 위해)
while i < len(family):                            # family 리스트의 요소 개수만큼 아래 명령문을 반복 (개수 4개)
    print("우리 가족에는", family[i], "(이)가 있습니다.")
    i+=1                                          # i를 1씩 증가시켜 4가될 때까지 반복