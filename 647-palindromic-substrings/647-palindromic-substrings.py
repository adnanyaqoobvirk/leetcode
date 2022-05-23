class Solution:
    def countSubstrings(self, s: str) -> int:
        def getPCounts(lo: int, hi: int) -> int:
            counts = 0
            while lo >= 0 and hi < n:
                if s[lo] != s[hi]:
                    break
                counts += 1
                lo, hi = lo - 1, hi + 1
            return counts
        
        n, ans = len(s), 0
        for i in range(n):
            ans += getPCounts(i, i) + getPCounts(i - 1, i)
        return ans