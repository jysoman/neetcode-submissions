class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []*2*len(nums)
        res[:len(nums)] = res[len(nums):] = nums
        return res