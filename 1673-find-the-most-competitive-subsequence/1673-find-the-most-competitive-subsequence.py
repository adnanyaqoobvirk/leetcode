class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        drops = len(nums) - k
        for num in nums:
            while stack and drops and stack[-1] > num:
                stack.pop()
                drops -= 1
            
            stack.append(num)
            
        while len(stack) > k:
            stack.pop()
            
        return stack