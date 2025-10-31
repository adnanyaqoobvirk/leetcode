class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += 1
        
        for i in range(n):
            nums[abs(nums[i]) - 1] *= -1
        
        ans = []
        for i in range(n):
            v = abs(nums[i]) - 1
            if nums[v] > 0:
                ans.append(v)
                nums[v] *= -1
        return ans