class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_to_dist = defaultdict(list)

        for point in points:
            dist = (point[0]**2 + point[1]**2)
            point_to_dist[dist].append(point)
        
        sorted_dists = sorted(point_to_dist.keys())

        res = []
        for d in sorted_dists:
            for p in point_to_dist[d]:
                if len(res) < k:
                    res.append(p)
        return res