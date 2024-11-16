class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        j = 0
        for i in range(1, k):
            if nums[i] <= nums[i - 1]:
                j = i
        
        ans = []
        for i in range(k - 1, len(nums)):
            if nums[i] <= nums[i - 1]:
                j = i
            if j > i - k + 1:
                ans.append(-1)
            else:
                ans.append(nums[i])
        return ans