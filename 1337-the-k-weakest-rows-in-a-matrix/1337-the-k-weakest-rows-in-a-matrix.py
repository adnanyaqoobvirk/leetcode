class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n, m = len(mat), len(mat[0])
        counts = {}
        for i in range(n):
            ones = 0
            for j in range(m):
                if mat[i][j] == 0:
                    break
                ones += 1
            counts.setdefault(ones, []).append(i)
        
        ans = []
        for j in range(m + 1):
            if j in counts:
                for i in sorted(counts[j]):
                    ans.append(i)
                    if len(ans) == k:
                        return ans