class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        max_num = 0
        for num in nums:
            num_map[num] += num
            max_num = max(max_num, num)
        
        dp = [0] * (max_num + 1)
        dp[1] = num_map[1]
        for num in range(2, max_num + 1):
            dp[num] = max(dp[num - 1], num_map[num] + dp[num - 2])
        return dp[max_num]