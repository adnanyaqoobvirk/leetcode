class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def valid(guess: int) -> bool:
            ops = 0
            for num in nums:
                ops += (num - 1) // guess
                if ops > maxOperations:
                    return False
            return True

        lo, hi = 0, max(nums)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if valid(mid):
                hi = mid
            else:
                lo = mid
        return hi