class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        R = 10 ** 9 + 7
        
        arr.append(-inf)
        
        ans = 0
        smallest = []
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                j = stack.pop()
                
                ans += (i - j) * (j - smallest[j]) * arr[j]
                ans %= R
                
            smallest.append(stack[-1] if stack else -1)
            stack.append(i)
        
        return ans