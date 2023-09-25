'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 카이사르 암호 --
        - 로마의 장군이 카이사르가 동맹군들과 소통하기 위해 만든 암호 (간단한 치환암호)
            알파벳 별로 인정한 거리만큼 밀어서 다른 알파벳으로 치환
            ex) 알파벳 a라면 3칸 이동한 d로 표기됨
'''
import string

src_str = string.ascii_uppercase            # _ 속성, 문자열에 있는 아스키코드 값을 대문자로 표현(소문자는 sower), 입력할 때 대문자로 입력해야함
dst_str = src_str[3:] + src_str[:3]         # 첫 시작은 [3:], 종료는 [ :3] (0, 1, 2) / + 는 연결을 의미, 첫 시작을 3번째로 하고 마지막을 2번째까지

def ciper(a):                               # ciper - 암호
    idx = src_str.index(a)                  # index - 위치를 찾음, 리스트 값 중 10을 입력하면 2번째 위치에 있는 1를 반환함
    return dst_str[idx]

src = input("대문자로 문장을 입력하세요 : ")
print("암호화 된 문장 : ", end='')

for ch in src:                              # 입력받은 src값을 ch에 반복하라, in 뒤에 있는 것을 순서대로 읽어오면서 반복
    if ch in src_str:                       # ch 값이 src_str 안에 포함된다면
        print(ciper(ch), end='')            # ciper 함수를 불러옴, ch는 매개변수, 함수 호출한 부분의 a 부분에 들어감(a도 매개변수)
    else:
        print(ch, end='')