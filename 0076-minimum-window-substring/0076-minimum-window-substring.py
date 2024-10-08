class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isEqual():
            for char, count in tcounts.items():
                if scounts[char] < count:
                    return False
            return True

        n, m = len(s), len(t)

        if n < m:
            return ""

        tcounts = Counter(t)
        scounts = Counter()
        rl, rr = 0, inf
        l = 0
        for r in range(n):
            scounts[s[r]] += 1

            while l <= r and isEqual():
                if r - l < rr - rl:
                    rl, rr = l, r
                scounts[s[l]] -= 1
                l += 1
        return s[rl:rr + 1] if rr != inf else ""

