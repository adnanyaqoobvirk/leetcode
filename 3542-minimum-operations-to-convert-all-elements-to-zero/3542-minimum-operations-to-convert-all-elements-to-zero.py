class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ops = 0
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
                ops += 1
            if not stack or stack[-1] != num:
                stack.append(num)
        while stack:
            num = stack.pop()
            if num != 0:
                ops += 1
        return ops