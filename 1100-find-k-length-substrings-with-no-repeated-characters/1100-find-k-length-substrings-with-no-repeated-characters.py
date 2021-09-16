class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        counts = {}
        ans = 0
        for i in range(len(s)):
            if i >= k:
                if counts[s[i - k]] == 1:
                    del counts[s[i - k]]
                else:
                    counts[s[i - k]] -= 1
            counts[s[i]] = counts.get(s[i], 0) + 1
            if len(counts) == k:
                ans += 1
        return ans