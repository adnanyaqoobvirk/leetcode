class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = sorted(Counter(tasks).values(), reverse=True)
        
        res = len(tasks)
        for i in range(min(len(freqs), n)):
            res = max(res, (freqs[i] - 1) * (n + 1) + 1 + i)
        
        return res