class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        triplets = 0
        for i in range(n - 2):
            remaining = target - nums[i]
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] < remaining:
                    triplets += r - l
                    l += 1
                else:
                    r -= 1
        return triplets