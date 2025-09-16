class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def getDistance(x: str, y: str) -> int:
            dcount = 0
            res = 0
            total = 0
            for r in range(n):
                if not (s[r] == x or s[r] == y):
                    if dcount < k:
                        dcount += 1
                        total += 1
                    else:
                        total -= 1
                else:
                    total += 1
                res = max(res, total)
            return res
        n = len(s)
        ans = 0
        for a, b in [("E", "N"), ("E", "S"), ("W", "N"), ("W", "S")]:
            ans = max(ans, getDistance(a, b))
        return ans