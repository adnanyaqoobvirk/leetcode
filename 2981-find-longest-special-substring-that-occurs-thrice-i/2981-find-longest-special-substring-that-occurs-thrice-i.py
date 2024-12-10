class Solution:
    def maximumLength(self, s: str) -> int:
        def valid(size: int) -> bool:
            counts = defaultdict(int)
            ch = ""
            count = 0
            for i in range(size):
                if ch != s[i]:
                    ch = s[i]
                    count = 1
                else:
                    count += 1
            
            if count == size:
                counts[ch] += 1
            
            for i in range(size, len(s)):
                if ch == s[i - size]:
                    count -= 1

                if ch != s[i]:
                    ch = s[i]
                    count = 1
                else:
                    count += 1
                
                if count == size:
                    counts[ch] += 1
                    if counts[ch] >= 3:
                        return True
            return False
        
        lo, hi = 1, len(s) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if valid(mid):
                lo = mid
            else:
                hi = mid
        return lo if valid(lo) else -1