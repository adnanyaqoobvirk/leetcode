class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        max_freq = 0
        for c in s:
            freq[c] += 1
            max_freq = max(max_freq, freq[c])
        
        buckets = [[] for _ in range(max_freq)]
        for c, i in freq.items():
            buckets[i - 1].append(c)
        
        ans = []
        for i in reversed(range(1, max_freq + 1)):
            for c in buckets[i - 1]:
                ans.extend([c] * i)
        return "".join(ans)