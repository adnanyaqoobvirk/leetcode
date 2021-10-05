class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = nums1[:m]
        second = nums2
        p = p1 = p2 = 0
        while p1 < m and p2 < n:
            if first[p1] <= second[p2]:
                nums1[p] = first[p1]
                p1 += 1
            else:
                nums1[p] = second[p2]
                p2 += 1
            p += 1
        
        p1, first, m = (p1, first, m) if p1 < m else (p2, second, n)
        while p1 < m:
            nums1[p] = first[p1]
            p += 1
            p1 += 1