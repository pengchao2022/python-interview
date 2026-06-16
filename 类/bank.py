# 定义一个类

class BankAccount(object):


    # 构造方法，函数初始化
    def __init__(self, account_numebr, account_name, balance=0):
        self.account_numebr = account_numebr
        self.account_name = account_name
        self.balance = balance
        self.transactions = [] # transactions 为转账记录，列表类型，默认为空


    # 方法一 存款
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"存款: +{amount}")
            print(f"您成功存款{amount} 元，当前余额为：{self.balance} 元")
        else:
            print("存款金额必须大于0") 


    # 方法二 取款
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"余额不足，您的取款金额为: {amount},但是当前余额为: {self.balance}")
        elif amount <= 0:
            print(f"取款金额必须大于0")
        else:
            self.balance -= amount
            self.transactions.append(f"取款: -{amount}")
            print(f"您成功取款{amount} 元，当起啊余额为: {self.balance} 元")


    # 方法三 显示余额
    def show_balance(self):
        print(f"当前余额为: {self.balance}")


    # 方法四 显示转账记录
    def show_transactions(self):
        for trans in self.transactions:
            print(f"   - {trans}")


# 创建对象
acc = BankAccount('621098', 'maxwell ma', 2000)

# 调用方法
# 调用存款方法
acc.deposit(0)

acc.deposit(900)

# 调用取款方法
acc.withdraw(2400)

acc.withdraw(9000)

# 调用显示余额方法
acc.show_balance()


# 调用转账记录方法
acc.show_transactions()



       