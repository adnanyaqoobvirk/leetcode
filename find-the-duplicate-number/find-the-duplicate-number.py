class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def numCount(num: int) -> int:
            count = 0
            for n in nums:
                if n <= num:
                    count += 1
            return count
        
        lo, hi = 1, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if numCount(mid) <= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo