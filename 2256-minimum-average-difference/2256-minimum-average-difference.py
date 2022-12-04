class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        min_diff, min_idx, n, curr_total, total = float('inf'), None, len(nums), 0, sum(nums)
        for i in range(n):
            curr_total += nums[i]
            avg_left = curr_total // (i + 1)
            avg_right = 0 if (n - i -1) == 0 else (total - curr_total) // (n - i - 1)
            diff = abs(avg_left - avg_right)
            if diff < min_diff:
                min_diff, min_idx = diff, i
        return min_idx