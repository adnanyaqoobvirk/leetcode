class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        prev, curr = [0], []
        for i in range(n):
            m = len(triangle[i])
            for j in range(m):
                curr.append(triangle[i][j] + min(prev[min(j, m - 2)], prev[max(0,j - 1)]))
            prev, curr = curr, []
        return min(prev)