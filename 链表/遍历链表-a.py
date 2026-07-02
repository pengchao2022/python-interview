# 遍历链表打印 1 -> 2 -> 3 - None

class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next


    # 定义方法遍历打印链表节点
    def print_linked_list(self):

        current = self
        result = []

        while current:
            result.append(str(current.val))
            current = current.next

        result.append('None')
        print('->'.join(result))


# 创建实例对象
head = ListNode(1)

head.next = ListNode(2)

head.next.next = ListNode(3)

# 调用方法
head.print_linked_list()


        