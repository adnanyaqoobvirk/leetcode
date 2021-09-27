class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n, m = len(mat), len(mat[0])
        counts = {}
        for i in range(n):
            left, right = 0, m
            while left < right:
                mid = left + (right - left >> 1)
                if mat[i][mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            counts.setdefault(left, []).append(i)
        
        ans = []
        for j in range(m + 1):
            indices = counts.get(j, [])
            if indices:
                for i in indices:
                    ans.append(i)
                    if len(ans) == k:
                        return ans