# 编写一个 Python 程序，
# 创建一个 Notebook 类，
# 在类内部维护一个笔记列表。
# 添加 add_note(note) 方法向列表中添加新笔记，以及 show_notes() 方法打印出所有已保存的笔记。

class Notebook:

    def __init__(self):
        self.notes = [] # 空列表


    def add_note(self, note):

        self.notes.append(note)

        print(f"已经添加笔记: {note}")
    

    def show_notes(self):

        if not self.notes:

            print("笔记为空！")

            return
        
        print("笔记列表:")
        for i, note in enumerate(self.notes, 1): # 1 表示从1 开始计数 而不是 0 
            print(f" {i}, {note}")


# 创建对象 实例
notebook = Notebook()

# 调用方法
notebook.add_note("buy a car")

notebook.add_note("buy a bike")

notebook.add_note("buy a house")

notebook.show_notes()



        

