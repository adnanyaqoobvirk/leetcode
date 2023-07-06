class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def valid(sl: int) -> bool:
            total = 0
            for i in range(sl):
                total += nums[i]
            
            if total >= target:
                return True
            
            left = 0
            for right in range(sl, len(nums)):
                total -= nums[left]
                total += nums[right]
                left += 1
                
                if total >= target:
                    return True
                
            return False
        
        l, r = 0, len(nums)
        while l + 1 < r:
            m = l + r >> 1
            if valid(m):
                r = m
            else:
                l = m
        
        if r == len(nums) and not valid(len(nums)):
            return 0
        else:
            return r