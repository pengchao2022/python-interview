# 从头到位打印链表所有值

class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next


    
    # 定义实例方法
    def print_list(self):

        current = self # self 就是当前节点
        while current:
            print(current.val)
            current = current.next

        
# 创建实例对象
head = ListNode(1)

head.next = ListNode(2)

head.next.next = ListNode(3)


# 调用方法
head.print_list()


        