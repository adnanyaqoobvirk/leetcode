class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts, i, ans = Counter(heights), 0, 0
        for h in range(1, 101):
            for _ in range(counts[h]):
                if heights[i] != h:
                    ans += 1
                i += 1
        return ans