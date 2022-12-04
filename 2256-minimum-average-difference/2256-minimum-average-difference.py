class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        avg_right, total = [0], 0
        for count, i in enumerate(reversed(range(len(nums))), 1):
            total += nums[i]
            avg_right.append(total // count)

        min_diff, min_idx, n, avg_left, total = float('inf'), None, len(nums), 0, 0
        for i in range(len(nums)):
            total += nums[i]
            avg_left = total // (i + 1)
            diff = abs(avg_left - avg_right[n - i - 1])
            if diff < min_diff:
                min_diff, min_idx = diff, i
        return min_idx