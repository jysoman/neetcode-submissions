class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close2open = {"}":"{", "]":"[", ")":"("}

        for char in s:
            if char not in close2open:
                stack.append(char)
            elif not stack or close2open[char] != stack.pop():
                return False

        return not stack