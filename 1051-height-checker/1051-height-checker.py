class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = Counter(heights)
        expected = []
        for i in range(1, 101):
            for _ in range(counts.get(i, 0)):
                expected.append(i)
        
        ans = 0
        for h, e in zip(heights, expected):
            if h != e:
                ans += 1
        return ans