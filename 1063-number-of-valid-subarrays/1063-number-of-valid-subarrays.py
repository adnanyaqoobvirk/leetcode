class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)
            ans += len(stack)
        return ans