class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char2freq = {}
        l = 0
        res = 0

        for r in range(len(s)):

            char2freq[s[r]] = 1 + char2freq.get(s[r], 0)

            while (r-l+1) - max(char2freq.values()) > k:
                #move left ptr
                char2freq[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res