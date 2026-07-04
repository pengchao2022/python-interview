# 题目要求：编写一个 Python 程序，创建一个 BankAccount 类，
# 包含一个 balance（余额）属性，
# 以及两个方法：deposit(amount) 
# 向账户存入金额，withdraw(amount) 从账户取款，
# 但取款金额不能超过当前余额（即余额不能小于 0）。

class BankAccount:

    # 构造方法 初始化函数 全局变量 balance 默认为0

    def __init__(self, balance=0):

        self.balance = balance



    # 方法一 定义存款方法 deposit()
    def deposit(self, amount): # amount 为局部变量
        if amount == 0:
            print("存款金额必须大于0")
            return

        self.balance += amount

        print(f"存款成功！ 成功存入{amount:.2f}元， 当前余额为: {self.balance:.2f}")

    # 方法二 定义取款方法 withdraw()
    def withdraw(self, amount):

        if amount <= 0:
            print("取款金额必须大于0")
            return
        
        if amount > self.balance:

            print(f"余额不足，当前余额为{self.balance:.2f} 您需要取的款项为: {amount:.2f}")

            return
        
        self.balance -= amount

        print(f"取款成功，成功取款: {amount:.2f}元，当前余额为: {self.balance}元")


# 创建对象实例
account = BankAccount(1000)

# 调用方法
account.deposit(2000)

account.withdraw(4000)



