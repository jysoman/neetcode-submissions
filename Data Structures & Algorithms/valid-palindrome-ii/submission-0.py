class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[:]==s[::-1]:
            return True
        else:
            for i in range(len(s)):
                temp = s[:i] + s[i+1:]
                # temp = temp.remove(c)
                if temp[:]==temp[::-1]:
                    return True
            return False