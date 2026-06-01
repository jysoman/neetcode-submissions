class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        res = 0
        curr=0

        while r < len(prices):
            if prices[l] <= prices[r]:
                curr = prices[r] - prices[l]
                res = max(res, curr)
                r+=1
            elif prices[r] < prices[l]:
                l = r
                r+=1
        return res