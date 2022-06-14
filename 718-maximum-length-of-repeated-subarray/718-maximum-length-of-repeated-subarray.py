class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        m, n = len(nums1), len(nums2)
        prev, curr = [0] * (n + 1), [0] * (n + 1)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if nums1[i] == nums2[j]:
                    curr[j] = prev[j + 1] + 1
                    ans = max(ans, curr[j])
            prev, curr = curr, [0] * (n + 1)
        return ans