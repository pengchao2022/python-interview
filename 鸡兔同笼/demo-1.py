# 编写一个程序，解决经典的"鸡兔同笼"问题：一个农场里有鸡和兔子，共 35 个头，94 条腿。问鸡和兔子各有多少只？

# 鸡兔同笼问题

# 鸡有 2 条腿 兔子有 4 条腿

# 总头数 = 35 ， 总腿数 = 94

def solve_chicken_rabbit(heads, legs):

    """
    解决鸡兔同笼问题
    Args:
        heads: 总头数
        legs: 总腿数

    Returns:
        tuple: (鸡的数量， 兔子的数量)

    """

    for rabbits in range(heads + 1):
        chickens = heads - rabbits
        if chickens * 2 + rabbits * 4 == legs:
            return chickens, rabbits
        

    return None

def run_app():

    heads = 35
    legs = 94

    result = solve_chicken_rabbit(heads, legs)

    if result:
        chickens, rabbits = result
        print(f"鸡: {chickens} 只")
        print(f"兔子: {rabbits} 只")
    else:
        print("无解")


run_app()
