class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = nums1
        n2 = nums2
        
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        
        while p1 >= 0 and p2 >= 0:
            if n1[p1] >= n2[p2]:
                nums1[p] = n1[p1]
                p1 -= 1
            else:
                nums1[p] = n2[p2]
                p2 -= 1
            p -= 1
        
        if p1 >= 0:
            for i in reversed(range(p1 + 1)):
                nums1[p] = n1[i]
                p -= 1
        else:
            for i in reversed(range(p2 + 1)):
                nums1[p] = n2[i]
                p -= 1