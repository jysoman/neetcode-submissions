class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""

        for char in s:
            if char.isalnum():
                res+=char.lower()
        return res[::1]==res[::-1]