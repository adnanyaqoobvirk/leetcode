class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        @cache
        def helper(v: int) -> int:
            if v <= 0:
                return 0
            if v == 1:
                num_map[1]
            
            return max(
                num_map[v] + helper(v - 2),
                helper(v - 1)
            )
        
        num_map = defaultdict(int)
        max_num = 0
        for num in nums:
            num_map[num] += num
            max_num = max(max_num, num)
        
        return helper(max_num)