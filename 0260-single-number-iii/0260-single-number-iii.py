class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        for num in nums:
            mask ^= num
        
        xmask = mask & -mask
        
        x = 0
        for num in nums:
            if num & xmask:
                x ^= num
        
        return [x, mask ^ x]