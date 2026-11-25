class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        mn, mx = arrays[0][0], arrays[0][-1]
        max_dist = 0
        for i in range(1, len(arrays)):
            max_dist = max(
                max_dist, abs(mx - arrays[i][0]), abs(arrays[i][-1] - mn)
            )
            mn, mx = min(mn, arrays[i][0]), max(mx, arrays[i][-1])
        return max_dist