class Solution:
    def maximumLength(self, s: str) -> int:
        def valid(size: int) -> bool:
            counts = defaultdict(int)
            j = 0
            for i in range(n):
                if i - j + 1 > size:
                    j += 1
                if s[j] != s[i]:
                    j = i
                if i - j + 1 == size:
                    counts[s[i] * size] += 1
            for c in counts.values():
                if c >= 3:
                    return True
            return False
        n = len(s)
        lo, hi = 1, len(s) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if valid(mid):
                lo = mid
            else:
                hi = mid
        return lo if valid(lo) else -1