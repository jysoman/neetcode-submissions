class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_to_cnt = {}

        for i in nums:
            val_to_cnt[i] = 1 + val_to_cnt.get(i,0)
        
        cnt_to_val = []

        for key,val in val_to_cnt.items():
            cnt_to_val.append([val,key])
        
        cnt_to_val.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(cnt_to_val[i][1])
        return res