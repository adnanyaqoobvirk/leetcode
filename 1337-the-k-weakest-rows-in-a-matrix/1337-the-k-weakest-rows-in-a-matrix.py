class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n, m = len(mat), len(mat[0])
        ans = {}
        for j in range(m + 1):
            for i in range(n):
                if i not in ans and (j == m or mat[i][j] == 0):
                    ans[i] = True
                if len(ans) == k:
                    return [k for k in ans.keys()]