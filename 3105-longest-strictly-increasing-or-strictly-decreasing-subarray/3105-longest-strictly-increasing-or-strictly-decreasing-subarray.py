class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = 1
        islen = dslen = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                islen = 0
            if nums[i] >= nums[i - 1]:
                dslen = 0
            islen += 1
            dslen += 1
            max_len = max(max_len, islen, dslen)
        return max_len