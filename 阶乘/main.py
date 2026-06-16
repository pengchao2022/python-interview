# calculate factorial 计算阶乘 

# e.g. 8*7*6*5*4*3*2*1


def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)
    

x = int(input("Please type your numebr here:"))
print(fact(x))


