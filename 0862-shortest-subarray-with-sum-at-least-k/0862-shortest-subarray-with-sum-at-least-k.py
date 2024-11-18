class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        h = []
        ans = inf
        psum = 0
        for i in range(len(nums)):
            psum += nums[i]
            while h and psum - h[0][0] >= k:
                _, j = heappop(h)
                ans = min(ans, i - j)
            heappush(h, (psum, i))
        while h:
            s, j = heappop(h)
            if s >= k:
                ans = min(ans, j + 1)
        return -1 if ans == inf else ans