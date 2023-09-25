class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for pos in range(32):
            mask = 1 << pos
            
            ones = 0
            for num in nums:
                if abs(num) & mask:
                    ones += 1
            if ones % 3:
                res |= mask
        return -res if sum(1 for num in nums if num < 0) % 3 else res