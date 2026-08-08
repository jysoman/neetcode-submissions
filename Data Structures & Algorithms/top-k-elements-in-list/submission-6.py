class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = {}
        freq_ct = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num in num2freq:
                num2freq[num] += 1
            else:
                num2freq[num] = 1

        for num, freq in num2freq.items():
            freq_ct[freq].append(num)
        res = []
        for i in range(len(freq_ct)-1, 0, -1):
            for n in freq_ct[i]:
                res.append(n)
                if len(res) == k:
                    return res
