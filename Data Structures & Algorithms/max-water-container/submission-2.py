class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                base = abs(j-i)
                height = min(heights[i], heights[j])
                vol = base*height
                res = max(res,vol)
        return res