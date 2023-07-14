class Solution:
    def longestSubsequence(self, a: List[int], d: int) -> int:
        depths, ans = defaultdict(int), 0
        for n in reversed(a):
            ndepth = depths[n] = depths[n + d] + 1
            ans = max(ans, ndepth)
        return ans