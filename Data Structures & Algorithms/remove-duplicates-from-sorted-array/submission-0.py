class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []

        for i in nums:
            if i not in seen:
                seen.append(i)
        
        nums[:len(seen)] = seen[:]
        return len(seen)