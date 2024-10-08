class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        if n < m:
            return ""

        tcounts = Counter(t)
        scounts = defaultdict(int)
        matches = 0
        rl, rr = 0, inf
        l = 0
        for r in range(n):
            scounts[s[r]] += 1
            if s[r] in tcounts and scounts[s[r]] == tcounts[s[r]]:
                matches += 1

            while l <= r and matches == len(tcounts):
                if r - l < rr - rl:
                    rl, rr = l, r
                scounts[s[l]] -= 1
                if s[l] in tcounts and scounts[s[l]] + 1 == tcounts[s[l]]:
                    matches -= 1
                l += 1
        return s[rl:rr + 1] if rr != inf else ""

