class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def search(row: List[int]) -> int:
            left, right = 0, m - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(n):
            j = search(grid[i])
            if j < m:
                count += (m - j)
        return count