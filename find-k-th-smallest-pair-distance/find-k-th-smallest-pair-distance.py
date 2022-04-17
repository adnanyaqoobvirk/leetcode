class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess: int) -> bool:
            count = left = 0
            for right, v in enumerate(nums):
                while v - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k
        
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            guess = lo + (hi - lo) // 2
            if possible(guess):
                hi = guess
            else:
                lo = guess + 1
        return lo