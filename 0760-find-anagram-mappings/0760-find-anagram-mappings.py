class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx_map = {num:i for i, num in enumerate(nums2)}
        return [idx_map[num] for num in nums1]