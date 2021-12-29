class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
        
        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                ans.append(i + 1)
        return ans