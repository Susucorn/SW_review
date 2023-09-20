'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- 버블 정렬 문제, 선택 정렬 --
'''

data = [90, 10, 23, 17, 56, 39]

def bubble(alist):
    for i in range(len(alist)-1):           # len 을 리스트에 쓰면 요소를 센다, 요소는 6개
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                tamp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = tamp

bubble(data)
print(data)