'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- atm 프로그램 --
'''

import sys
pin = 1234      # 핀 번호 선언
balance = 0     # 잔액

# 예금
def get_balance():
    global balance  
    amount = int(input("입금하실 금액을 입력해주세요 : "))
    balance = amount + balance
    print("입금하신 금액은 {}원, 잔액은 총 {}원 입니다.".format(amount, balance))

# 인출
def widthdraw():
    global balance
    amount = int(input("출금하실 금액을 입력해주세요 : "))
    if amount > balance:
        print(f"잔액이 부족합니다. 현재 잔액은 {balance}원 입니다.")
    else:
        balance = balance - amount
        print(f"출금이 완료되었습니다. 현재 잔액은 총 {balance}원 입니다.")

# 잔액보기
def view_balance():
    global balance
    print(f"현재 잔액은 총 {balance}원 입니다.")

user_pin = int(input("암호를 입력하세요 : "))
if pin != user_pin:
    print("암호가 잘못되었습니다.")
    sys.exit()

while True:
    move = int(input("사용할 동작을 선택하세요 : | 1- 잔액보기 | | 2- 입금하기 | | 3- 인출하기 | | 4- 종료 | : "))
    if move == 1:      # 이 조건을 만족한다면 함수 호출
        view_balance()   
    elif move == 2:
        get_balance()
    elif move == 3:
        widthdraw()
    elif move == 4:
        print("이용해주셔서 감사합니다.")
        sys.exit()