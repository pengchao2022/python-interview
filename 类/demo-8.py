# 定义一个自定义异常类，该类接受一个字符串消息作为属性。

class InsufficientBalanceError(Exception):

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"当前余额: {balance}, 需要: {amount}"
        super().__init__(message)


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        
        else:
            self.balance -= amount
            print(f"取款成功！剩余：{self.balance}")


# 创建对象实例
account = BankAccount(200)

try:
    account.withdraw(300)

except InsufficientBalanceError as e:
    print(e)


