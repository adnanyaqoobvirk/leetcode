class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        @cache
        def helper(num: int) -> int:
            if num > max_num:
                return 0
            
            return max(
                num_map[num] + helper(num + 2),
                helper(num + 1)
            )
        
        max_num, num_map = 0, defaultdict(int)
        for num in nums:
            num_map[num] += num
            max_num = max(max_num, num)
        
        return helper(0)
        