class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.append(0)
        
        n = len(nums)
        
        left = total = 0
        for right in range(n):
            total += nums[right]
            if total >= target:
                break
        
        ans = inf
        for right in range(right + 1, n):
            while total >= target:
                total -= nums[left]
                left += 1
            ans = min(ans, right - left + 1)
            total += nums[right]
        return 0 if ans == inf else ans