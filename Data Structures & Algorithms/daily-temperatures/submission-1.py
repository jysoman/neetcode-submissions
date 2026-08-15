class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] # ind, temp
        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][1]:
                s_ind, s_tmp = stack.pop()
                res[s_ind] = i - s_ind
            stack.append([i, tmp])
        return res