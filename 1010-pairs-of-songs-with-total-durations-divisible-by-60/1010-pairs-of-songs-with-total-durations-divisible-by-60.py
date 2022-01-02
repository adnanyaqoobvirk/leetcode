class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts, ans = defaultdict(int), 0
        for t in time:
            r = t % 60
            if r == 0:
                ans += counts[0]
            else:
                ans += counts[60 - r]
            counts[r] += 1
        return ans