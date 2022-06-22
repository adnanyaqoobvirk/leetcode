class Solution:
    def specialArray(self, nums: List[int]) -> int:
        lo, hi = 1, max(nums)
        while lo <= hi:
            guess = lo + (hi - lo) // 2
            
            greater = 0
            for num in nums:
                if num >= guess:
                    greater += 1
                    
            if greater == guess:
                return guess
            elif greater < guess:
                hi = guess - 1
            else:
                lo = guess + 1
        return -1