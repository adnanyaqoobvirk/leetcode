class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = Counter(heights)
        ans = pos = 0
        for i in range(1, 101):
            for _ in range(counts.get(i, 0)):
                if heights[pos] != i:
                    ans += 1
                pos += 1
        return ans