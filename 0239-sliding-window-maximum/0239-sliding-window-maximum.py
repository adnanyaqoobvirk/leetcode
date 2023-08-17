class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            
        ans = [nums[q[0]]]
        for i in range(k, len(nums)):
            start = i - k + 1
            
            while q and q[0] < start:
                q.popleft()
                
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)
            ans.append(nums[q[0]])
        return ans