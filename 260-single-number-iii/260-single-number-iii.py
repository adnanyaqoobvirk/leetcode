class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        for num in nums:
            mask ^= num
        mask = mask & -mask
        
        first = 0
        for num in nums:
            if mask & num:
                first ^= num
                
        second = 0
        for num in nums:
            if num != first:
                second ^= num
        return [first, second]