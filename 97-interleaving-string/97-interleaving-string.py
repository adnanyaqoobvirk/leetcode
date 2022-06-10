class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def helper(p1: int, p2: int, p3: int) -> bool:
            if p1 == n1 and p2 == n2 and p3 == n3:
                return True
            
            if p3 == n3:
                return False
            
            ans = False
            if p1 < n1 and s1[p1] == s3[p3]:
                ans |= helper(p1 + 1, p2, p3 + 1)
            
            if p2 < n2 and s2[p2] == s3[p3]:
                ans |= helper(p1, p2 + 1, p3 + 1)
            return ans
        n1, n2, n3 = len(s1), len(s2), len(s3)
        return helper(0, 0, 0)