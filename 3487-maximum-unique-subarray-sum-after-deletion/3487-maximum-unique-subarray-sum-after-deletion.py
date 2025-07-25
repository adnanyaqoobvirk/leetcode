class Solution:
    def maxSum(self, nums: List[int]) -> int:
        total = max(nums)
        seen = {total}
        for num in nums:
            if num < 0:
                continue
            if num not in seen:
                total += num
                seen.add(num)
        return total
