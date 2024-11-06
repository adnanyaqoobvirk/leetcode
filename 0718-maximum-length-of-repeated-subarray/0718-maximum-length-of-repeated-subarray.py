class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        P, M = 127, 10**9 + 7

        def valid(l: int) -> bool:
            rhash1 = rhash2 = 0
            pmax = 1
            for i in range(l):
                if i > 0:
                    pmax = pmax * P % M
                rhash1 = (rhash1 * P + nums1[i]) % M
                rhash2 = (rhash2 * P + nums2[i]) % M
            
            seen = {rhash1}
            for i in range(l, len(nums1)):
                rhash1 -= nums1[i - l] * pmax
                rhash1 = rhash1 * P + nums1[i]

                seen.add(rhash1)
            
            if rhash2 in seen:
                return True

            for i in range(l, len(nums2)):
                rhash2 -= nums2[i - l] * pmax
                rhash2 = rhash2 * P + nums2[i]

                if rhash2 in seen:
                    return True
            return False

        lo, hi = 0, min(len(nums1), len(nums2)) + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if valid(mid):
                lo = mid
            else:
                hi = mid
        return lo