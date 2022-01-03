class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        
        degrees = [0] * (n + 1)
        for p, j in trust:
            degrees[j] += 1
            degrees[p] -= 1
        
        for i in range(1, n + 1):
            if degrees[i] == n - 1:
                return i
        return -1