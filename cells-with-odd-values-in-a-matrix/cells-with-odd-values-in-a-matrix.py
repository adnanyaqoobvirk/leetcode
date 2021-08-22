class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_counts = {}
        col_counts = {}
        for r, c in indices:
            row_counts[r] = row_counts.get(r, 0) + 1
            col_counts[c] = col_counts.get(c, 0) + 1
        
        odd_count = 0
        for i in range(m):
            for j in range(n):
                if (row_counts.get(i, 0) + col_counts.get(j, 0)) % 2 != 0:
                    odd_count += 1
        return odd_count