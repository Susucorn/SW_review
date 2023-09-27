'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 피그 라틴 암호  --
        맨 앞의 자음을 엄로 돌리고 그 뒤에 ay를 붙이는 일종의 말장난
            ex) boy --> oy + b + ay --> oybay
'''

word = input("단어를 입력하세요 : ")

first = word[0]     # 대문자 0번째
new_word = word[1:] + first + "ay"

print(new_word)