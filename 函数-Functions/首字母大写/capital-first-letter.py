# 输入一个语句，将英文语句里面每隔单词大写

def capitalize_word(text):

    words = text.split() # 以任意空白分割

    new_words = []

    for word in words:

        capitalized = word[0].upper() + word[1::].lower()

        new_words.append(capitalized)

    
    return ' '.join(new_words)


def run_app():

    text = input("请在此输入您的语句: \n")

    new_text = capitalize_word(text)

    print(new_text)


if __name__ == "__main__":

    run_app()

    

    

