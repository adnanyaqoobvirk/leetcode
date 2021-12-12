class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def helper(pos: int, curr_total: int) -> bool:
            if curr_total == total_half:
                return True
            
            if pos == n:
                return False
            
            return helper(pos + 1, curr_total + nums[pos]) or helper(pos + 1, curr_total)
        
        total = sum(nums)
        if total & 1: 
            return False
        
        n, total_half = len(nums), total // 2
        return helper(0, 0)