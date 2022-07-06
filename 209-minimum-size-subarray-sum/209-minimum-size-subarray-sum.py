class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def isSumEqualGreater(l: int) -> bool:
            total = 0
            for i in range(l):
                total += nums[i]
            
            for j in range(i + 1, len(nums)):
                if total >= target:
                    return True
                
                total -= nums[j - l]
                total += nums[j]
            return total >= target
        
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isSumEqualGreater(mid + 1):
                hi = mid
            else:
                lo = mid + 1
        return 0 if lo == len(nums) else lo + 1