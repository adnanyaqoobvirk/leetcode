class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        min_ops = inf
        counts = {}
        l = 0
        for r in range(n):
            counts[nums[r]] = counts.get(nums[r], 0) + 1

            while nums[l] + n - 1 < nums[r]:
                counts[nums[l]] -= 1
                if counts[nums[l]] == 0:
                    del counts[nums[l]]
                l += 1
            min_ops = min(min_ops, n - len(counts))
        return min_ops