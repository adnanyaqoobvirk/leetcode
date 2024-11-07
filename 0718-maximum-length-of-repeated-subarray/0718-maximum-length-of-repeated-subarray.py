class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if nums2 > nums1:
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        prev, curr = [0] * (n + 1), [0] * (n + 1)
        ans = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    curr[j + 1] = 1 + prev[j]
                    ans = max(ans, curr[j + 1])
                prev[j] = 0
            prev, curr = curr, prev
        return ans