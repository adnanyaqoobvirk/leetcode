class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = [nums1[i] for i in range(m)]
        n2 = nums2
        
        p = p1 = p2 = 0
        while p1 < m and p2 < n:
            if n1[p1] <= n2[p2]:
                nums1[p] = n1[p1]
                p1 += 1
            else:
                nums1[p] = n2[p2]
                p2 += 1
            p += 1
        
        if p1 < m:
            for i in range(p1, m):
                nums1[p] = n1[i]
                p += 1
        else:
            for i in range(p2, n):
                nums1[p] = n2[i]
                p += 1