class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        ans = 0
        for i in range(len(nums)):
            j = bisect_left(nums, lower - nums[i], i + 1)
            k = bisect_right(nums, upper - nums[i], i + 1)
            ans += k - j
        return ans