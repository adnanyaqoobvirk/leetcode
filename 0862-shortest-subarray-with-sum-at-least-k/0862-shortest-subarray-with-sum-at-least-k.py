class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        h = []
        ans = inf
        psum = 0
        for i in range(len(nums)):
            psum += nums[i]
            if psum >= k:
                ans = min(ans, i + 1)
            while h and psum - h[0][0] >= k:
                _, j = heappop(h)
                ans = min(ans, i - j)
            heappush(h, (psum, i))
        return -1 if ans == inf else ans