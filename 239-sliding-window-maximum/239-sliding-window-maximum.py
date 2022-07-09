class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = [(-nums[i], i) for i in range(k)]
        heapify(window)
        
        ans = [-window[0][0]]
        for i in range(k, len(nums)):
            while window and window[0][1] <= (i - k):
                heappop(window)
            heappush(window, (-nums[i], i))
            ans.append(-window[0][0])
        return ans