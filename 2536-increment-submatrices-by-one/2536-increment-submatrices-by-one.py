class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        for x1, y1, x2, y2 in queries:
            for x in range(x1, x2 + 1):
                ans[x][y1] += 1
                if y2 + 1 < n:
                    ans[x][y2 + 1] -= 1
        
        for x in range(n):
            total = 0
            for y in range(n):
                total += ans[x][y]
                ans[x][y] = total
        return ans