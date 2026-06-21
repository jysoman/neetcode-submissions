class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        C2P = {i:[] for i in range(numCourses)}
        visit =set()

        for crs, pre in prerequisites:
            C2P[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return False
            if C2P[crs]==[]:
                return True
            visit.add(crs)

            for pre in C2P[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            C2P[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True