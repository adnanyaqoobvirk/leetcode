class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            
        node_color = {}
        
        stack = [source]
        while stack:
            curr = stack[-1]
            
            if curr in node_color:
                if node_color[curr] == 0:
                    for child in graph[curr]:
                        if node_color.get(child, 0) != 1:
                            return False
                    node_color[curr] = 1
                stack.pop()
                continue
                    
            if not graph[curr] and curr != destination:
                return False
            
            node_color[curr] = 0
            for child in graph[curr]:
                stack.append(child)
        return True