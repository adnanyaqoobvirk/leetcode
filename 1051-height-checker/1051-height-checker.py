class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected, ans = sorted(heights), 0
        for e, h in zip(expected, heights):
            if e != h:
                ans += 1
        return ans