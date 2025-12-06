class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        window = SortedList()
        dp = [0] * (n + 1)
        dp[0] = 1
        j = 0
        prefix_sum = 0
        for i in range(n):
            window.add(nums[i])
            prefix_sum += dp[i]

            while j < i and (window[-1] - window[0]) > k:
                window.remove(nums[j])
                prefix_sum -= dp[j]
                j += 1
            
            dp[i + 1] = (dp[i + 1] + prefix_sum) % MOD
        return dp[n]