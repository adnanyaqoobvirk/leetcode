class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def possible(wsize: int) -> bool:
            wcounts = counts.copy()
            for i in range(wsize):
                wcounts[s[i]] -= 1
            
            for c in "abc":
                if wcounts[c] < k:
                    break
            else:
                return True
            
            for i in range(wsize, n):
                wcounts[s[i]] -= 1
                wcounts[s[i - wsize]] += 1
                for c in "abc":
                    if wcounts[c] < k:
                        break
                else:
                    return True
            return False

        counts = Counter(s)
        n = len(s)
        lo, hi = 0, n + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if possible(mid):
                lo = mid
            else:
                hi = mid
        return n - lo if possible(lo) else -1