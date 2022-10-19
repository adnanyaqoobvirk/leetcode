class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def helper(size: int) -> bool:
            total = 0
            for i in range(size):
                total += nums[i]
            
            left, right = 0, i + 1
            while right < n:
                if total >= target:
                    return True
                total -= nums[left]
                total += nums[right]
                left += 1
                right += 1
            return total >= target
        
        n = len(nums)
        l, r = 1, n + 1
        while l < r:
            m = l + (r - l) // 2
            
            if helper(m):
                r = m
            else:
                l = m + 1
        return l if l != n + 1 else 0