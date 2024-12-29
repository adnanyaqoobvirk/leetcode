class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        total = 0
        max_idx = -1
        ans = -inf
        for i, num in enumerate(nums):
            if max_idx == -1 or abs(num) > abs(nums[max_idx]):
                if max_idx != -1:
                    total -= abs(nums[max_idx]) ** 2
                    total += nums[max_idx]
                total += abs(num) ** 2 
                max_idx = i
            elif nums[max_idx] >= 0 and num < 0 and abs(num) == abs(nums[max_idx]):
                total -= abs(nums[max_idx]) ** 2
                total += nums[max_idx]
                total += abs(num) ** 2 
                max_idx = i
            else:
               total = max(total + num, num)
            ans = max(ans, total)
        return ans 