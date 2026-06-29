class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapped = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in mapped and stack:
                if stack[-1]==mapped[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True

