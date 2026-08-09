class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = -1
        if len(s) < 2:
            return len(s)
        start, end = 0, 1
        char2pos={}
        char2pos[s[start]] = 0
        while start < end and end <= len(s)-1:
            if s[end] in char2pos and char2pos[s[end]] >= start:
                start = char2pos[s[end]]+1
            
            char2pos[s[end]] = end
            
            max_len = max(max_len, end-start+1)
            end += 1

        return max_len