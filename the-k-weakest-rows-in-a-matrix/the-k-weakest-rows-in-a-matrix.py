class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def soldierCount(row: int) -> int:
            lo, hi = 0, n - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if row[mid] == 1:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo if row[lo] == 0 else lo + 1
        
        m, n = len(mat), len(mat[0])
        h = [(soldierCount(row), i) for i, row in enumerate(mat)]
        heapify(h)
        return [heappop(h)[1] for _ in range(k)]