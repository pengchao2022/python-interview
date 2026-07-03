# 输入一个句子，将句子里面的空格替换为下划线

def replace_space(sentence):

    return sentence.replace(' ', '_')


def run_app():

    sentence = input("请在此输入您的句子: \n")

    new_sentence = replace_space(sentence)


    print(new_sentence)


if __name__ == "__main__":

    run_app()

    