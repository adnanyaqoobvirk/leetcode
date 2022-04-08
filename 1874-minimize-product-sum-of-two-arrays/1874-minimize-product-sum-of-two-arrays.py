class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        return sum(
            n1 * n2 
            for n1, n2 in zip(
                sorted(nums1), 
                sorted(nums2, reverse=True)
            )
        )