'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 전역변수와 지역변수 --
    [구조] def 함수명():
               명령문
'''

a = 10

def func_a():
    num = 1
    num = num + a
    print(num)

func_a()
print(a)
# print(num) => 에러가 남, num은 지역변수이기 때문에 정의되지 않은 값