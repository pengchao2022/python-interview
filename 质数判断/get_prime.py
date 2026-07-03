# 输入一个整数，获取给定整数范围内的质数，并每隔一个打印出来

# ----------------------------------
# 质数 是指 只能被 1 和自己 整数的数

# 是整数

# 大于 1
# ----------------------------------

# 判断一个数是否为 质数
def is_prime(n):

    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False
        
    return True

# 准备质数列表
def get_alternate_primes(limit_number):

    primes = []

    for num in range(2, limit_number + 1):

        if is_prime(num):

            primes.append(num) # 得到所有质数的列表

    
    # 每隔一个质数打印
    result = primes[::2] # 步长为 2

    return result

def run_app():

    limit_number = int(input("请在此输入您要打印质数的范围: \n").strip())

    expect_primes = get_alternate_primes(limit_number)

    print(expect_primes)


if __name__ == "__main__":

    run_app()

    



