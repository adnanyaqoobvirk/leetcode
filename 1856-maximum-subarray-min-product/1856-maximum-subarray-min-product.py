class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        R = 10 ** 9 + 7
        n = len(nums)
        
        smallest = [-1] * n
        stack = []
        prefix = []
        total = 0
        for i in range(n):
            total += nums[i]
            prefix.append(total)
            
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if stack:
                smallest[i] = stack[-1]
            
            stack.append(i)
        
        ans = 0
        stack = []
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            p = prefix[stack[-1] - 1] if stack else prefix[-1]
            ans = max(ans, (p - (prefix[smallest[i]] if smallest[i] != -1 else 0)) * nums[i])
            
            stack.append(i)
        return ans % R
            