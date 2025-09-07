class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for num in nums:
            while stack and stack[-1] < num:
                if len(stack) >= 2:
                    ans += 1
                stack.pop()
            stack.append(num)
        return ans