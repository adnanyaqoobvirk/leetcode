class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if n1 + n2 != n3:
            return False
        
        prev, curr = [False] * (n2 + 1), [False] * (n2 + 1)
        for p1 in reversed(range(n1 + 1)):
            for p2 in reversed(range(n2 + 1)):
                p3 = p1 + p2
                
                if p1 == n1 and p2 == n2 and p3 == n3:
                    curr[p2] = True
                else:
                    curr[p2] = False
                    if p1 < n1 and s1[p1] == s3[p3]:
                        curr[p2] |= prev[p2]

                    if p2 < n2 and s2[p2] == s3[p3]:
                        curr[p2] |= curr[p2 + 1]
            prev, curr = curr, prev
        return prev[0]
        