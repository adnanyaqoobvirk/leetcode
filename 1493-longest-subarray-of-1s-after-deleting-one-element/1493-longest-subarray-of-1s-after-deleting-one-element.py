class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        nxt = -1
        for j in range(n):
            if nums[j] == 0:
                nxt = j
                break
                
        ans = cur = 0
        for i in range(j + 1, n):
            if nums[i] == 0:
                ans = max(ans, i - cur - 1)
                cur, nxt = nxt + 1, i
        
        return max(ans, n - cur - 1)