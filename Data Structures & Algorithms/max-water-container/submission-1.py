class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #max dist between 2 and maximize the height of the smallest
        start, end = 0, len(heights)-1
        maxarea=0
        while start != end:
            cont_height = min(heights[start], heights[end])
            cont_length = end - start
            area = cont_height*cont_length
            maxarea = max(maxarea, area)
            # move the pointer for smaller height value
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
        return maxarea