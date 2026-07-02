# 编写一个程序 判断输入的年份是否是闰年

# 闰年的判断规则

# 1， 能被 400 整除

# 2， 能被 4 整除 但是不能被 100 整除

def is_leap_year(year):

    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def run_app():

    year = int(input("请在此输入您要判断的年份:").strip())

    determine = is_leap_year(year)

    if determine:

        print(f"{year} 是闰年")

    else:

        print(f"{year} 不是闰年")


if __name__ == "__main__":

    run_app()

    