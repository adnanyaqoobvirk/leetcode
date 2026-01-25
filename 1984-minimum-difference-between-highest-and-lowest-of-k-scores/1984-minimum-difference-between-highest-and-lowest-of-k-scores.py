class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        min_diff = inf
        for r in range(len(nums)):
            while r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                min_diff = min(nums[r] - nums[l], min_diff)
        return min_diff