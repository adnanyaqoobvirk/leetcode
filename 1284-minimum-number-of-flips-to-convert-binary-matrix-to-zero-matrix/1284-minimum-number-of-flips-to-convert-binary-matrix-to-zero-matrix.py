from typing import Any

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def toggle(x: int, y: int) -> None:
            for k, l in [(x, y), (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= k < m and 0 <= l < n:
                    mat[k][l] ^= 1
        @cache
        def backtrack(i: int, j: int, mt: Any) -> int:
            if mt == zmat:
                return 0
            
            ans = float('inf')
            if (mt, i, j) not in seen:
                seen.add((mt, i, j))
                for x in range(m):
                    for y in range(n):
                        toggle(x, y)
                        smt = tuple([tuple(mat[a]) for a in range(m)])
                        res = backtrack(x, y, smt) + 1
                        if res:
                            ans = min(ans, res)
                        toggle(x, y)
                if (mt, i, j) in seen:
                    seen.remove((mt, i, j))
            return -1 if ans == float('inf') else ans
        
        m, n = len(mat), len(mat[0])
        zmat = tuple([tuple([0] * n) for _ in range(m)])
        seen = set()
        return backtrack(0, 0, tuple([tuple(mat[a]) for a in range(m)]))