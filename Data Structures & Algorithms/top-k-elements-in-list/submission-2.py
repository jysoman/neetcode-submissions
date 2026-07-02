class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #find unique numbers
        unique_nums = set(nums)
        num_freq = {}
        if k == len(unique_nums):
            return list(unique_nums)
        #sort them by frequency
        for num_i in nums:
            if num_i in num_freq:
                num_freq[num_i] += 1
            else:
                num_freq[num_i] = 1
        
        #get the top freq
        sorted_freq = list(sorted(num_freq.values(), reverse=True))[:k]

        output = [k for k,v in num_freq.items() if v in sorted_freq]
        return output

        #return top k