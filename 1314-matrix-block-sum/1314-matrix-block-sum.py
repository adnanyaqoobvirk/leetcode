class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        h, w = len(mat) + 1, len(mat[0]) + 1
        
        ii = [[0] * w for _ in range(h)]
        for y in range(1, h):
            for x in range(1, w):
                ii[y][x] = mat[y - 1][x - 1] + ii[y][x - 1] + ii[y - 1][x] - ii[y - 1][x - 1]
        
        ans = [[0] * (w - 1) for _ in range(h - 1)]
        for y in range(1, h):
            by_min, by_max = max(y - k, 1), min(y + k, h - 1)
            for x in range(1, w):
                bx_min, bx_max = max(x - k, 1), min(x + k, w - 1)
                ans[y - 1][x - 1] = ii[by_max][bx_max] - ii[by_min - 1][bx_max] - ii[by_max][bx_min - 1] + ii[by_min - 1][bx_min - 1]
        return ans