class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        partition_count = 0
        curr_sum = 0
        for i in range(len(nums) - 1):
            curr_sum += nums[i]
            if abs(curr_sum - total + curr_sum) & 1:
                continue
            partition_count += 1
        return partition_count