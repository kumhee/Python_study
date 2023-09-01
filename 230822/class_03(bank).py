# Account - (AtmAccount, bankAccount, CreditAccount)
# Atm = 현금 입출금 -> 5만원권, 1만원권, 5천원, 1천원
#   현금이 얼마지 세서 계좌에 입금, 출금은 지폐 어떤 것들로 해서 사용자한테 줄지를 정해주는 것
# Bank = 예금 이자 (최저금액 이상 이자) - 일정 금액 이상이 넘으면 이자 발생
# Credit = 결제 (한도초과)

class Account:
    def __init__(self, accountNumber = "1234", balance = 0) :
        self._accountNumber = accountNumber
        self._balance = balance
        
    def getBalance(self) :
        return self._balance

    def deposite(self, amount) :
        if amount < 0 :
            print("잘못된 입력입니다.")
            return
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0 or amount > self._balance:
            print("잘못된 입력입니다. 잔액이 부족합니다.")
            return
        self._balance = amount
        
        
    



class Atm(Account):
    money = 1000000
    def __init__(self):
        super().__init__()
        
    def cash(self):
        while True:
            print("원하시는 업무를 선택해주세요.")
            print("1. 잔액확인")
            print("2. 출금")
            print("3. 입금")
            
            menu = input('입력: ')
            
            if menu == "1" :
                print(f"잔액은 {self.money}원 입니다")
                break
            elif menu == "2":
                get = int(input('출금할 금액을 입력해주세요'))
                if self.money < get :
                    print('금액이 부족합니다.')
                else:                  
                    self.money -= get
                    
                    cash_50000 = (get // 50000) #50000
                    get -= cash_50000 * 50000
                    cash_10000 = (get // 10000) #10000
                    get -= cash_50000 * 10000
                    
                    print(f'50000원권은 {cash_50000}장, 10000원권은 {cash_10000}장 입니다.')
                    print(f'출금 후 잔액은 {self.money}원 입니다.')
                break
            elif menu == "3":
                set = int(input('입금할 금액을 입력하세요.'))
                self.money += set
                print(f'입금 후 잔액은 {self.money}입니다')    
                break
    
    
    
class Bank(Account):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0
        
    def interest(self):
        bank_deposit = int(input("예금하실 금액을 입력해주세요:"))
        
        if bank_deposit >= 100000:
            self.interest_rate  = bank_deposit ** 0.05
            print(f"적용금리는 {self.interest_rate}원 입니다.")
        else :
            print("잘못된 입력입니다. ")


class Credit(Account):
    cardLimit = 10000000
    def __init__(self):
        super().__init__()
    
    def overLimit(self) :
        print("원하시는 업무를 선택해주세요.")
        print("1. 한도조회")
        print("2. 결제")
            
        pay = input('입력:')
        if pay == "1" :
            print(f"카드 한도는 {self.cardLimit}원 입니다")
        elif pay == "2" :
            payCount = int(input('금액을 입력해주세요:'))
            if payCount > 10000000 :
                print("한도초과입니다.")
            elif payCount < 10000000 :
                self.cardLimit -= payCount
                print("결제가 완료되었습니다")
                print(f'잔액은 {self.cardLimit}입니다')
        else :
            print("오류")
        
        
        
print()     
account = Account()
account.deposite(1000000)
print("account의 잔액은:", account.getBalance(), "원 입니다.")



print()
atm_account = Atm()
atm_account.cash()



print()
bank_account = Bank()
bank_account.interest()



print()
credit_account = Credit()
credit_account.overLimit()