class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            ops = 0
            for num in nums:
                ops += (num - 1) // mid
            
            if ops > maxOperations:
                lo = mid + 1
            else:
                hi = mid
        return lo