class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def getKMin(a: int, b: int) -> int:
            if k == 1:
                return 0
                
            nums = set()
            for x in range(a, a + k):
                for y in range(b, b + k):
                    nums.add(grid[x][y])
            nums = sorted(nums)
            ans = inf
            for i in range(len(nums) - 1):
                ans = min(ans, abs(nums[i + 1] - nums[i]))
            return 0 if ans == inf else ans

        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                row.append(getKMin(i, j))
            ans.append(row)
        return ans