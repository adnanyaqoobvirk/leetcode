class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        ans = nums[-1]
        q = deque([(nums[-1], n - 1)])
        for i in reversed(range(n - 1)):
            while q and q[0][1] > i + k:
                q.popleft()
            
            ans = nums[i] + q[0][0]
            
            while q and q[-1][0] < ans:
                q.pop()
            q.append((ans, i))
        return ans