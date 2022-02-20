class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for x in s:
            # 注意 不可以用 x == '(' or '[' and '{' 可以if '[' == '(' or '[' == '[' or '[' == '{':
            # 左括号，入栈
            if x in ['(','{','[']:
                res.append(x)
            # 右括号 弹出栈顶元素
            else:
                if res:
                    top =  res.pop()
                else:
                    return False
                if x == ')' and top!= '(':
                    return False
                if x == ']' and top!= '[':
                    return False
                if x == '}' and top!= '{':
                    return False
        return not res

# 优化一下 使用键值对
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        for i in s:
            if i in dict:
                stack.append(i)
            else:
                if stack:
                    if stack.pop() != dict[i]:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True