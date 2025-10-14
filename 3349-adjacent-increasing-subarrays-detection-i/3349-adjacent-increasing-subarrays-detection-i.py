class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(k, n - k + 1):
            for j in range(1, k):
                if nums[i - k + j] <= nums[i - k + j - 1]:
                    break
                if nums[i + j] >= nums[i + j + 1]:
                    break
            else:
                return True
        return False