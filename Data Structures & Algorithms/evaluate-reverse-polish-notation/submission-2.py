class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c=='+':
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                stack.append(temp1+temp2)
                continue
            if c=='-':
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                stack.append(temp2-temp1)
                continue
            if c=='*':
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                stack.append(temp1*temp2)
                continue
            if c=='/':
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                stack.append(int(temp2/temp1))
                continue
            stack.append(c)
        return int(stack[-1])