class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def possible(guess: int) -> bool:
            count, total = 1, 0
            for num in nums:
                total += num
                if total > guess:
                    count += 1
                    total = num
            return count <= m
        
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            guess = lo + (hi - lo) // 2
            if possible(guess):
                hi = guess
            else:
                lo = guess + 1
        return lo