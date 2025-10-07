class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        full = {}
        l = 0
        for r in range(n):
            if rains[r] > 0:
                if rains[r] in full:
                    l = max(l, full[rains[r]] + 1)
                    while l < r and rains[l] != 0:
                        l += 1
                    if l == r:
                        return []
                    ans[l] = rains[r]
                    l += 1
                full[rains[r]] = r
            else:
                ans[r] = 1
        return ans


                        