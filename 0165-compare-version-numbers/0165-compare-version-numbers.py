class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        
        n, m = len(v1), len(v2)
        
        for i in range(max(n, m)):
            if i < n and i < m:
                if v1[i] < v2[i]:
                    return -1
                elif v1[i] > v2[i]:
                    return 1
            elif i < n and v1[i] > 0:
                return 1
            elif i < m and v2[i] > 0:
                return -1
        return 0