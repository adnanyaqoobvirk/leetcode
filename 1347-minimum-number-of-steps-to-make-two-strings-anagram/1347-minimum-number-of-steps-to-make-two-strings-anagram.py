class Solution:
    def minSteps(self, s: str, t: str) -> int:
        tcounts = Counter(t)
        ans = 0
        for c in s:
            count = tcounts.get(c, 0)
            if count == 0:
                ans += 1
            else:
                tcounts[c] = count - 1
        return ans