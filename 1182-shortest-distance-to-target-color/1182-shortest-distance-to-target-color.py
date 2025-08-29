class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        dis = [[inf] * 3 for _ in range(n)]
        ci = [inf] * 3
        for i in range(n):
            ci[colors[i] - 1] = i
            for c in range(3):
                if ci[c] != inf:
                    dis[i][c] = i - ci[c]
        ci = [inf] * 3
        for i in reversed(range(n)):
            ci[colors[i] - 1] = i
            for c in range(3):
                if ci[c] != inf:
                    dis[i][c] = min(dis[i][c], ci[c] - i)
        return [dis[i][c - 1] if dis[i][c - 1] != inf else -1 for i, c in queries]