class Solution:
    def frequencySort(self, s: str) -> str:
        ans = []
        for c, freq in sorted(Counter(s).items(), key = lambda t: t[1], reverse = True):
            ans.extend([c] * freq)
        return "".join(ans)