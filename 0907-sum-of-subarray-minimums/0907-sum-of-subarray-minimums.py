class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        R = 10 ** 9 + 7
        N = len(arr)
        
        smallest = [N] * N
        stack = []
        for i in reversed(range(N)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
                
            if stack:
                smallest[i] = stack[-1]
            
            stack.append(i)
            
        ans = 0
        stack = []
        for i in range(N):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            count = (i - stack[-1]) if stack else (i + 1)
            ans += (smallest[i] - i) * count * arr[i]
            ans %= R
            
            stack.append(i)
        return ans