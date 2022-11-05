class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        for i in reversed(range(len(nums) - 1)):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            stack.append(nums[i])
        
        ans = [-1] * len(nums)
        for i in reversed(range(len(nums))):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
        
        return ans