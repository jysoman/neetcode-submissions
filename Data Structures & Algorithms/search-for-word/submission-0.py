class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(x,y,i):
            if i == len(word):
                return True
            if (min(x,y)<0 or x>=rows or y>=cols or (x,y)in visit or
                word[i]!=board[x][y]):
                return False
            visit.add((x,y))

            res = ( dfs(x+1,y,i+1) or
                    dfs(x-1,y,i+1) or
                    dfs(x,y+1,i+1) or
                    dfs(x,y-1,i+1))
            visit.remove((x,y))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False