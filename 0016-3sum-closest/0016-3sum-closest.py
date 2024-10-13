class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        ans = inf
        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(total - target):
                    ans = total

                if total > target:
                    r -= 1
                else:
                    l += 1
        return ans