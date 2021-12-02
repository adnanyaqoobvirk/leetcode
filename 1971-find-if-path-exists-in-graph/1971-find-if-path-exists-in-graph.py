class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        stack = [start]
        visited = set()
        while stack:
            curr = stack.pop()
            visited.add(curr)
            for v in graph[curr]:
                if v == end:
                    return True
                if v not in visited:
                    stack.append(v)
        return start == end