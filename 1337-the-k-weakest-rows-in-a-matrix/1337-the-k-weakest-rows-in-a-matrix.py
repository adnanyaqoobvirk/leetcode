class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n, m = len(mat), len(mat[0])
        done = set()
        ans = []
        for j in range(m + 1):
            for i in range(n):
                if i not in done and (j == m or mat[i][j] == 0):
                    ans.append(i)
                    done.add(i)
                if len(ans) == k:
                    return ans