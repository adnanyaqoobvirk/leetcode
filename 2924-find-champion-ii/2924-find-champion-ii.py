class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for a, b in edges:
            indegree[b] += 1
        ans = -1
        for i in range(n):
            if indegree[i] == 0:
                if ans != -1:
                    return -1
                ans = i
        return ans