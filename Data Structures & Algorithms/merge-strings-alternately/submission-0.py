class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1,p2 = 0,0
        min_len = min(len(word1),len(word2))
        res = ""
        while p1 < min_len:
            res+=word1[p1]
            res+=word2[p1]
            p1+=1
        if len(word1) > len(word2):
            res+=word1[p1:]
        if len(word2) > len(word1):
            res+=word2[p1:]
        return res