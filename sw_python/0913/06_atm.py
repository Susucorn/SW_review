'''
    신라대학교 202395016 컴퓨터공학부 박수연

    -- ATM기 프로그램 --
'''
import sys

amount = 0      # 입력하는 금액
balance = 0     # 잔액
pin = 1234      # 암호

# 첫번째 함수
def get_balance():  # get_balance 함수, 잔액조회 함수
    global balance  # 어디서나 쓸 수 있는 변수
    print(f"잔액은 {balance} 입니다.")

# 두번째 함수
def deposit():
    global balance
    amount = int(input("입금하실 금액을 입력하세요 : "))
    balance = balance + amount                          # 잔액 + 입금할 돈
    print(f"현재 잔액은 {balance}입니다.")

# 세번째 함수
def widthdraw():
    global balance
    amount = int(input("인출하실 금액을 입력해주세요 : "))
    amount = balance - amount
    if amount > balance:
        print("잔액이 부족합니다.")
    print(f"현재 잔액은 {balance}입니다.")

user_pin = int(input("암호를 입력하세요 : "))
if pin != user_pin:
    print("암호가 잘못되었습니다.")
    sys.exit()

while True:
    query = int(input("사용할 동작을 선택하세요 : | 1-잔액보기 | | 2- 입금하기 | | 3- 인출하기 | | 4- 종료 | "))
    if query == 1:      # 이 조건을 만족한다면 함수 호출
        get_balance()   
    elif query == 2:
        deposit()
    elif query == 3:
        widthdraw()
    elif query ==4:
        sys.exit