class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        curr, prev = [0] * (n + 1), [0] * (n + 1)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                lines = prev[j]
                for k in range(j, n):
                    if nums1[i] == nums2[k]:
                        lines = max(lines, 1 + prev[k + 1])
                curr[j] = lines
            prev, curr = curr, prev
        return prev[0]