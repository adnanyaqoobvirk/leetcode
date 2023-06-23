class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        mn, mx = arrays[0][0], arrays[0][-1] 
        for i in range(1, len(arrays)):
            first, last = arrays[i][0], arrays[i][-1]
            ans = max(ans, abs(mx - first), abs(mn - last))
            mx = max(mx, last)
            mn = min(mn, first)
        return ans