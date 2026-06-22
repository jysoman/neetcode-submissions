class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()

            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            else:
                stones[-1] = stones[-1] - stones[-2]
                stones.remove(stones[-2])
        if stones:
            return stones[0]
        else:
            return 0
