class BankAccount:
    def __init__(self, owner):
        self.owner=owner
        self.__balance=0
        print(f"{self.owner} 계좌가 생성되었습니다.")

    def set_balance(self, amount):
        if self.__balance >= 0:
            self.__balance = amount

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if self.__balance >= 0:
            self.__balance += amount
            print("통장에서 {self.owner.amount}원이 입금되었습니다.")
    
    def withdraw(self, amount):
        if self.__balance >= self.owner.get_balance():
            self.__blance = 0
        else: 
            self.__balance -= amount
            print("통장에서 {self.owner.amount}원이 출금되었습니다.")

a= BankAccount("A")
b = BankAccount("B")

a.deposit(100)
b.deposit(200)
a.withdraw(30)
b.withdraw(50)

print(f"{a.owner} 계좌의 현재 잔액:", a.get_balance())
print(f"{b.owner} 계좌의 현재 잔액:", b.get_balance())

a.set_balance(500)
print(f"{a.owner} 계좌의 수정된 잔액:", a.get_balance())