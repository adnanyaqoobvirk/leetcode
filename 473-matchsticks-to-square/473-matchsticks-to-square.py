class Solution:
    def makesquare(self, nums):
        @cache
        def helper(mask: int) -> int:
            if mask == 0: return 0
            for j in range(n):
                if mask & 1<<j:
                    neib = helper(mask ^ 1<<j)
                    if neib >= 0 and neib + nums[j] <= basket:
                        return (neib + nums[j]) % basket
            return -1
        
        n = len(nums)
        basket, rem = divmod(sum(nums), 4)
        if rem or max(nums) > basket: return False
        return helper((1<<n) - 1) == 0