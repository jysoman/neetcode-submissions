class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_to_freq = {}

        for num in nums:
            n_to_freq[num] = 1 + n_to_freq.get(num, 0)
        
        freq_to_num = []

        for num, freq in n_to_freq.items():
            freq_to_num.append([freq,num])
        freq_to_num.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(freq_to_num[i][1])
        return res

