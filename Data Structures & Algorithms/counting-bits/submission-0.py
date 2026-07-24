class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(i):
            res = 0
            while i:
                if i%2:
                    res+=1
                i //= 2
            return res
        res = []
        
        for num in range(n+1):
            res.append(count(num))
        return res