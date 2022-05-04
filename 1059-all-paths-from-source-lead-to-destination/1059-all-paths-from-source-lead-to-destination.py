class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for src, dst in edges:
            graph[src].add(dst)
        
        visited, stack = {}, [source]
        while stack:
            curr = stack[-1]
            
            if not graph[curr] and curr != destination:
                return False
            
            for node in graph[curr]:
                if node not in visited or not visited[node]:
                    break
            else:
                visited[curr] = True
                stack.pop()
                continue

            visited[curr] = False
            for node in graph[curr]:
                if node in visited and not visited[node]:
                    return False
                stack.append(node)
        return True
        