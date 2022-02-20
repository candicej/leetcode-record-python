# 将一个栈当作输入栈，用于压入 push 传入的数据；另一个栈当作输出栈，用于 pop 和 peek 操作。
# 每次 pop 或 peek 时，若输出栈为空则将输入栈的全部数据依次弹出并压入输出栈，这样输出栈从栈顶往栈底的顺序就是队列从队首往队尾的顺序。
class MyQueue:

    def __init__(self):
        self.stackin = []
        self.stackout = []


    def push(self, x: int) -> None:
        self.stackin.append(x)


    def pop(self) -> int:
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
        return self.stackout.pop()

    def peek(self) -> int:
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
        return self.stackout[-1]

    def empty(self) -> bool:
        return not self.stackin and not self.stackout



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()