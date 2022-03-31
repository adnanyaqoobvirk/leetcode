class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def splitPossible(total: int) -> bool:
            curr = splits = 0
            for num in nums:
                if curr + num > total:
                    curr = num
                    splits += 1
                else:
                    curr += num
            return curr <= total and splits < m
        
        n, lo, hi = len(nums), max(nums), sum(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if splitPossible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo