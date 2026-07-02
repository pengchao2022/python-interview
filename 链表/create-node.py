# 创建链表 创建3个节点

class ListNode(object):

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next



# 创建 3 个节点
node1 = ListNode(1)

node2 = ListNode(2)

node3 = ListNode(3)

node1.next = node2

node2.next = node3

# 验证
print(node1.val)

print(node1.next.val)

print(node1.next.next.val)


        