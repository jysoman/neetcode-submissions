class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}

        for char in s:
            hm1[char] = hm1.get(char, 0) + 1
        
        for char in t:
            hm2[char] = hm2.get(char, 0) + 1

        return hm1 == hm2