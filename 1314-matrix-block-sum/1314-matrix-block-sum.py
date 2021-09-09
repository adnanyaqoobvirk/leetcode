class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        h, w = len(mat), len(mat[0])
        
        ii = [[0] * w for _ in range(h)]
        for y in range(h):
            total = 0
            for x in range(w):
                total += mat[y][x]
                ii[y][x] = total
                if y > 0:
                    ii[y][x] += ii[y - 1][x]
        
        ans = [[0] * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                bx_min, by_min = max(x - k, 0), max(y - k, 0)
                bx_max, by_max = min(x + k, w - 1), min(y + k, h - 1)
                
                ans[y][x] = ii[by_max][bx_max]
                
                if by_min > 0:
                    ans[y][x] -= ii[by_min - 1][bx_max]
                
                if bx_min > 0:
                    ans[y][x] -= ii[by_max][bx_min - 1]
                
                if by_min > 0 and bx_min > 0:
                    ans[y][x] += ii[by_min - 1][bx_min - 1]
        return ans