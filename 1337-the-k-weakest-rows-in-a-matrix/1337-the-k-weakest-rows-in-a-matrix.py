class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n, m = len(mat), len(mat[0])
        counts = {}
        for i in range(n):
            left, right = 0, m - 1
            while left < right:
                mid = left + (right - left) // 2
                if mat[i][mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            counts.setdefault(left if mat[i][left] == 0 else left + 1, []).append(i)
        
        ans = []
        for j in range(m + 1):
            indices = counts.get(j, [])
            if indices:
                indices.sort()
                for i in indices:
                    ans.append(i)
                    if len(ans) == k:
                        return ans