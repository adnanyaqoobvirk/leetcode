class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            mask = 1
            while num & mask:
                mask <<= 1
            value = num ^ (mask >> 1)
            if value != num:
                res.append(value)
            else:
                res.append(-1)
        return res