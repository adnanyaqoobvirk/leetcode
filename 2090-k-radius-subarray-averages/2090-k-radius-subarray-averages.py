class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        wsize = 2 * k + 1
        ans = [-1] * len(nums)
        left = total = 0
        for right in range(len(nums)):
            total += nums[right]
            if right - left + 1 == wsize:
                ans[right - k] = total // wsize
                total -= nums[left]
                left += 1
        return ans