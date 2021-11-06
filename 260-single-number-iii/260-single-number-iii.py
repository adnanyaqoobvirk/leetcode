class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        for num in nums:
            mask ^= num
            
        first_mask = mask & -mask
        
        first = 0
        for num in nums:
            if first_mask & num:
                first ^= num
        return [first, mask ^ first]