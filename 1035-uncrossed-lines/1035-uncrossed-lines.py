class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0
            
            lines = dp(i + 1, j)
            for k in range(j, n):
                if nums1[i] == nums2[k]:
                    lines = max(lines, 1 + dp(i + 1, k + 1))
            return lines
        
        m, n = len(nums1), len(nums2)
        return dp(0, 0)