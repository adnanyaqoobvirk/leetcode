class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        max_pair_sum = 0
        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - i - 1]
            if pair_sum > max_pair_sum:
                max_pair_sum = pair_sum
        return max_pair_sum
            