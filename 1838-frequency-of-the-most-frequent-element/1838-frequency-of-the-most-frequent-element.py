class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        def freq(t: int) -> int:
            max_len = 0
            ops = k
            l = 0
            for r in range(n):
                ops -= abs(t - nums[r])

                if ops < 0:
                    ops += abs(t - nums[l])
                    l += 1
                
                if ops >= 0:
                    max_len = max(max_len, r - l + 1)
            return max_len 

        nums.sort()
        n = len(nums)

        lo, hi = min(nums), max(nums) + k + 1
        ans = 0
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            f1 = freq(mid)
            f2 = freq(mid + 1)
            if f2 > f1:
                lo = mid
            else:
                hi = mid
        return freq(lo)