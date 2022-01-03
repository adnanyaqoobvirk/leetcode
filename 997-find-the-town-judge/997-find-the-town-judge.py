class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        
        indegrees = [0] * (n + 1)
        outdegrees = [0] * (n + 1)
        for p, j in trust:
            indegrees[j] += 1
            outdegrees[p] += 1
        
        for i in range(1, n + 1):
            if indegrees[i] == n - 1 and outdegrees[i] == 0:
                return i
        return -1