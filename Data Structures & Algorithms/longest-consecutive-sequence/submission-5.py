class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_len = 0
        
        for num in nums:
            seq_len = 0
            if num-1 not in numset:
                seq_len = 1
                while num + seq_len in numset:
                    seq_len += 1
                max_len = max(max_len, seq_len)
            
        return max_len
        

        