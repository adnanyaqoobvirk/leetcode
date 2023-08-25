class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dp(p1: int, p2: int) -> bool:
            p3 = p1 + p2
            
            if p3 == n3:
                return True
            
            if p1 == n1:
                if s2[p2] == s3[p3]:
                    return dp(p1, p2 + 1)
                else:
                    return False
                
            if p2 == n2:
                if s1[p1] == s3[p3]:
                    return dp(p1 + 1, p2)
                else:
                    return False
            
            res1 = dp(p1 + 1, p2) if s1[p1] == s3[p3] else False
            res2 = dp(p1, p2 + 1) if s2[p2] == s3[p3] else False

            return res1 or res2
        
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        return dp(0, 0)