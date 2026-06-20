# 输入一连串英文语句，要求统计出所有大写字母的个数和小些字母的个数

def count_upper_lower_cases(sentence):

    # 初始化

    upper = 0
    lower = 0

    for char in sentence:

        if char.isupper():
            upper += 1

        elif char.islower():
            lower += 1

    return upper, lower


def run_app():

    user_sentence = input("请在此输入一连串英文语句:")

    upper, lower = count_upper_lower_cases(user_sentence)

    print(f"总共有 {upper} 个英文大写字母")

    print(f"总共有 {lower} 个小写字母")



run_app()


