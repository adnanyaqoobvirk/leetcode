class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        prev, curr = [0] * (n + 1), [0] * (n + 1)
        ans = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    curr[j + 1] = 1 + prev[j]
                    ans = max(ans, curr[j + 1])
            prev, curr = curr, prev
        return ans