class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans, nums2_counts = [], Counter(nums2)
        for num, count in Counter(nums1).items():
            for _ in range(min(count, nums2_counts[num])):
                ans.append(num)
        return ans