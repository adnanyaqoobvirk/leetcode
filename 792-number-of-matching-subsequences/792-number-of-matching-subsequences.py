class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        for i, c in enumerate(s):
            buckets[c].append(i)
        
        ans = 0
        for word in words:
            i = 0
            for c in word:
                b = buckets[c]
                lo, hi = 0, len(b)
                while lo < hi:
                    mid = lo + (hi - lo) // 2
                    if b[mid] >= i:
                        hi = mid
                    else:
                        lo = mid + 1
                if lo == len(b):
                    break
                i = b[lo] + 1
            else:
                ans += 1
        return ans