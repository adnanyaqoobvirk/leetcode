class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num, num_map = 0, defaultdict(int)
        for num in nums:
            num_map[num] += num
            max_num = max(max_num, num)
        
        dp = [0] * (max_num + 3)
        for num in reversed(range(max_num + 1)):
            dp[num] = max(
                num_map[num] + dp[num + 2],
                dp[num + 1]
            )
        return dp[0]