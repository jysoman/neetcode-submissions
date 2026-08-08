class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort all the intervals by start time
        create a res array
        go through intervals, see if overlap, then merge
        else add to res
        """
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
