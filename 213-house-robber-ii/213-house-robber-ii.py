class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        ans = 0
        for start, m in [(0, n - 1), (1, n)]:
            prev = curr = 0
            for pos in range(start, m):
                prev, curr = curr, max(nums[pos] + prev, curr)
            ans = max(ans, curr)
        return ans