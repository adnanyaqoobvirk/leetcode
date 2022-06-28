class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        @cache
        def helper(num: int) -> int:
            if num > max_val:
                return 0
            
            if num not in counts:
                return helper(num + 1)
            
            return max(
                num * counts[num] + helper(num + 2),
                helper(num + 1)
            )
        
        min_val, max_val, counts = min(nums), max(nums), Counter(nums)
        return helper(min_val)