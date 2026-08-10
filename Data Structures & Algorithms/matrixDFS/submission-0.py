class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def dfs(mat, r, c, crossed):
            ROW, COL = len(mat), len(mat[0])
            if r < 0 or c < 0 or r == ROW or c == COL or mat[r][c] == 1 or (r,c) in crossed:
                return 0

            if r == ROW - 1 and c == COL - 1:
                return 1

            crossed.add((r,c))
            count = 0
            count += dfs(mat, r-1, c, crossed)
            count += dfs(mat, r+1, c, crossed)
            count += dfs(mat, r, c-1, crossed)
            count += dfs(mat, r, c+1, crossed)

            crossed.remove((r,c))
            return count


        return dfs(grid, 0, 0, set())