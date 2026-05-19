class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        j = 0
        for i in range(len(nums1)):
            while j < len(nums2) and nums1[i] >= nums2[j]:
                if nums1[i] == nums2[j]:
                    return nums1[i]
                j += 1
        
        return -1