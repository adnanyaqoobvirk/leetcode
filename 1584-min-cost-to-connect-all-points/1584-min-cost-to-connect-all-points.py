class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, ans = len(points), 0
        edges, visited, not_visited, i = [], {0}, set(range(n)), 0
        while len(visited) < n:
            for j in not_visited:
                (xi, yi), (xj, yj) = points[i], points[j]
                heappush(edges, (abs(xi - xj) + abs(yi - yj), j))
            while edges[0][1] in visited: heappop(edges)
            d, i = heappop(edges)
            visited.add(i)
            not_visited.discard(i)
            ans += d
        return ans