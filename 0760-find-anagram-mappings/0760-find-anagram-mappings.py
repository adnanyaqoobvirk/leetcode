class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx_map = defaultdict(list)
        for i, num in enumerate(nums2):
            idx_map[num].append(i)
        return [idx_map[num].pop() for num in nums1]