class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            nums[i] = -nums[i]
        
        ans = []
        for num in nums:
            i = abs(num) - 1
            if nums[i] > 0:
                ans.append(abs(num))
                nums[i] = -nums[i]
        return ans