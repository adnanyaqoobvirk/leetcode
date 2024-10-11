class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        triplets = 0
        for i in reversed(range(n)):
            for j in reversed(range(i)):
                k = bisect_left(nums, target - nums[i] - nums[j], 0, j)
                triplets += k
        return triplets