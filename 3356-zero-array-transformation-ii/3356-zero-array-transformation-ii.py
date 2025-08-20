class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def valid(k: int) -> bool:
            diffs = [0] * (m + 1)
            for i in range(k):
                l, r, v = queries[i]
                diffs[l] -= v
                diffs[r + 1] += v
            
            t = 0
            for i in range(m):
                t += diffs[i]
                if t + nums[i] > 0:
                    return False
            return True
        
        m = len(nums)
        n = len(queries)
        lo, hi = -1, n
        while lo + 1 < hi:
            guess = lo + (hi - lo) // 2
        
            if valid(guess):
                hi = guess
            else:
                lo = guess
        return hi if valid(hi) else -1