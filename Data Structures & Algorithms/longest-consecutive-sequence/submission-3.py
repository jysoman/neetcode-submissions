class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        curr=1
        for i in nums:
            if i-1 not in nums:
                curr = 1
                while i+1 in nums:
                    curr+=1
                    i+=1
            res = max(res,curr)
        return res