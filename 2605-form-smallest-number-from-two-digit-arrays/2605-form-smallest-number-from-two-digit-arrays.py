class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        if common:
            return min(common)

        min1, min2 = min(nums1), min(nums2)
        if min1 > min2:
            return min2 * 10 + min1
        else:
            return min1 * 10 +  min2