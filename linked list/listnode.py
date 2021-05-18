class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList( head):
    #
    if head is None or head.next is None:
        return head

    print("头节点的值")
    a = head.next.val
    p = reverseList(head.next)
    head.next.next = head
    head.next = None

    print("p节点的值")
    b = p.val
    print(p.val)
    return p

# 将列表转换成链表
def stringToListNode(input):
    numbers = input
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)# 分别将列表中每个数转换成节点
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr


# 将链表转换成字符串
def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    lis = stringToListNode(head)
    re_list = reverseList(lis)
    print(listNodeToString)