class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row):
            l,r = 0, len(row)-1

            while l<=r:
                mid = (l+r)//2
                if row[mid] < target:
                    l = mid+1
                elif row[mid] > target:
                    r = mid-1
                else:
                    return True
            return False
        
        for row in matrix:
            if binary_search(row):
                return True
        return False  