class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        counts = Counter(nums)
        if counts[1] > 0:
            return n - counts[1]
        
        min_len = inf
        for i in range(n):
            curr_gcd = nums[i]
            for j in range(i + 1, n):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        return -1 if min_len == inf else min_len + n - 2