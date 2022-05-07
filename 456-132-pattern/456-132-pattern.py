class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minis, mini = [], float('inf')
        for num in nums:
            mini = min(mini, num)
            minis.append(mini)
        
        stack = []
        for j in reversed(range(len(nums))):
            while stack and stack[-1] <= minis[j]:
                stack.pop()
            
            if stack and stack[-1] < nums[j]:
                return True
            
            if nums[j] > minis[j]:
                stack.append(nums[j])

        return False