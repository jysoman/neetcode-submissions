class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxL,maxR = 0 , 0
        res = nums[0]
        cursum = 0
        l = 0
        
        for r in range(len(nums)):
            if cursum < 0:
                cursum = 0
                l = r

            cursum += nums[r]
            res = max(res,cursum)
        return res  