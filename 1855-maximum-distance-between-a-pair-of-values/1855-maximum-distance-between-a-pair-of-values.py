class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        
        max_d = 0
        for i in range(len(nums1)):
            lo, hi = i, n
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums1[i] <= nums2[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            max_d = max(max_d, lo - i - 1)
        return max_d