class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        ans = inf
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                psum = nums[i] + nums[j]
                diff = target - psum
                k = bisect_right(nums, diff, j + 1)
                if k < n and abs(diff - nums[k]) < abs(target - ans):
                    ans = psum + nums[k]
                if k > j + 1 and abs(diff - nums[k - 1]) < abs(target - ans):
                    ans = psum + nums[k - 1]
        return ans