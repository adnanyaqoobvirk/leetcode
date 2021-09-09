class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        h, w = len(mat), len(mat[0])
        
        ii = [[0] * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                ii[y][x] = mat[y][x]
                if x > 0:
                    ii[y][x] += ii[y][x - 1]
                if y > 0:
                    ii[y][x] += ii[y - 1][x]
                if x > 0 and y > 0:
                    ii[y][x] -= ii[y - 1][x - 1]
        
        ans = [[0] * w for _ in range(h)]
        for y in range(h):
            by_min, by_max = max(y - k, 0), min(y + k, h - 1)
            for x in range(w):
                bx_min, bx_max = max(x - k, 0), min(x + k, w - 1)
                ans[y][x] = ii[by_max][bx_max]
                if by_min > 0:
                    ans[y][x] -= ii[by_min - 1][bx_max]
                if bx_min > 0:
                    ans[y][x] -= ii[by_max][bx_min - 1]
                if by_min > 0 and bx_min > 0:
                    ans[y][x] += ii[by_min - 1][bx_min - 1]
        return ans