class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        avg_left, total = [], 0
        for i, num in enumerate(nums, 1):
            total += num
            avg_left.append(total // i)

        avg_right, total = [0], 0
        for count, i in enumerate(range(len(nums) - 1, 0, -1), 1):
            total += nums[i]
            avg_right.append(total // count)

        min_diff, min_idx, n = float('inf'), None, len(nums)
        for i in range(len(nums)):
            diff = abs(avg_left[i] - avg_right[n - i - 1])
            if diff < min_diff:
                min_diff, min_idx = diff, i
        return min_idx