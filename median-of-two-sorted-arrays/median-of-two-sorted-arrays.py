class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        n, m = len(nums1), len(nums2)
        mid = (n + m) // 2
        lo, hi = 0, n
        while lo <= hi:
            xmid = (lo + hi) // 2
            ymid = mid - xmid
            
            lx = float('-inf') if xmid == 0 else nums1[xmid - 1]
            rx = float('inf') if xmid == n else nums1[xmid] 
            
            ly = float('-inf') if ymid == 0 else nums2[ymid - 1]
            ry = float('inf') if ymid == m else nums2[ymid] 
            
            if lx > ry:
                hi = xmid - 1
            elif ly > rx:
                lo = xmid + 1
            elif (n + m) & 1:
                return min(rx, ry)
            else:
                return (min(rx, ry) + max(lx, ly)) / 2