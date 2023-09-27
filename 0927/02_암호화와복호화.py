'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 암호화와 복호화 --
'''
plain_text = "Love will find a way."    # 평문
encrypted_text = ""                     # 암호문

for c in plain_text:
    x = ord(c)
    x += 1                              # 65를 입력받았다면 +1 해서 66이 됨
    cc = chr(x)                         # 숫자를 문자형으로 바꿈 (65 = a --> 66 = b)
    encrypted_text = encrypted_text + cc

print(encrypted_text)

# 복호화 코드
'''
encrypted_text = "Mpwf!xjmm!gjoe!b!xbz/"    # 평문
plain_text = ""                     # 암호문

for c in plain_text:
    x = ord(c)
    x -= 1                              # 65를 입력받았다면 +1 해서 66이 됨
    cc = chr(x)                         # 숫자를 문자형으로 바꿈 (65 = a --> 66 = b)
    plain_text = plain_text + cc

print(plain_text)
'''