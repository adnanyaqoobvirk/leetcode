class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def linked(x: List[int], y: List[int]) -> bool:
            return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2) <= x[2]
        
        def dfs(curr: int) -> int:
            ans = 1
            for node in graph[curr]:
                if node not in visited:
                    visited.add(node)
                    ans += dfs(node)
            return ans
        
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                if linked(bombs[i], bombs[j]):
                    graph[i].append(j)
                if linked(bombs[j], bombs[i]):
                    graph[j].append(i)
        
        res = 0
        for i in range(len(bombs)):
            visited = {i}
            res = max(res, dfs(i))
        return res