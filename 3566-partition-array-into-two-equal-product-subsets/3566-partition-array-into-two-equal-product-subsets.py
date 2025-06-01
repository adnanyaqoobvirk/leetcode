class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        def dp(i: int, t1: int, t2: int) -> bool:
            if i == n: 
                return t1 == 1 and t2 == 1
            
            if nums[i] == 0:
                return False
            
            res = False
            if t1 % nums[i] == 0:
                res = res or dp(i + 1, t1 // nums[i], t2)
            
            if t2 % nums[i] == 0:
                res = res or dp(i + 1, t1, t2 // nums[i])

            return res
            
        n = len(nums)
        return dp(0, target, target)