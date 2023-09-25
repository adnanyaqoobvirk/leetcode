class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        p, pcount = -inf, 3
        for c in nums:
            if c != p:
                if pcount < 3:
                    return p
                pcount = 0
            p = c
            pcount += 1
        return p