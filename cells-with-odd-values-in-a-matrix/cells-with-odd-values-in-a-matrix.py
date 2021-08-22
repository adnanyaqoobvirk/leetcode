class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        odd_rows = defaultdict(bool)
        odd_cols = defaultdict(bool)
        odd_rows_count = 0
        odd_cols_count = 0
        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
            odd_rows_count += 1 if odd_rows[r] else -1
            odd_cols_count += 1 if odd_cols[c] else -1
        return (m - odd_rows_count) * odd_cols_count + (n - odd_cols_count) * odd_rows_count