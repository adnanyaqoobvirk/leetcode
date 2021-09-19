class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = abs(nums[i] - nums[j])
                if diff == k:
                    ans += 1
                elif diff > k:
                    break
        return ans