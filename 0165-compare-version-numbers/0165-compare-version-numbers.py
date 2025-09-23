class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split(".")
        revisions2 = version2.split(".")
        m, n = len(revisions1), len(revisions2)

        for i in range(max(m, n)):
            r1, r2 = 0, 0
            if i < m:
                r1 = int(revisions1[i])
            if i < n:
                r2 = int(revisions2[i])
                
            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1
        return 0