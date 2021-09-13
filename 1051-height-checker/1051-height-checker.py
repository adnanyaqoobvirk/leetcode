class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for h, e in zip(heights, expected):
            if h != e:
                ans += 1
        return ans