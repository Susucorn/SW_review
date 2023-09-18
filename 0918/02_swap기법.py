'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- swap 기법 --
'''
# 숫자 바꾸기
a1 = 10
b1 = 20

def swap(a, b):
    global a1, b1
    t = a1
    a1 = b1
    b1 = t

print(a1, b1)
swap(a1, b1)
print(a1, b1)

# 숫자가 바뀌지 않는 코드, global 하지 않음
a2 = 10
b2 = 20

def swap(a, b):
    t = a
    a = b
    b = t

print(a2, b2)
swap(a2, b2)
print(a2, b2)