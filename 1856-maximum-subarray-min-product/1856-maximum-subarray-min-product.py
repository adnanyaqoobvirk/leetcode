class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        R = 10 ** 9 + 7
        n = len(nums)
        
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        
        smallest = [n] * n
        stack = []
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if stack:
                smallest[i] = stack[-1]
            
            stack.append(i)
        
        ans = 0
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            p = prefix[stack[-1]] if stack else 0
            ans = max(ans, (prefix[smallest[i] - 1] - p) * nums[i])
            
            stack.append(i)
        return ans % R
            