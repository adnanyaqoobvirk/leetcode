class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def helper(curr: int) -> bool:
            if curr in node_color:
                return node_color[curr] == 1
            
            if not graph[curr] and curr != destination:
                return False
            
            node_color[curr] = 0
            for child in graph[curr]:
                if not helper(child):
                    return False
            node_color[curr] = 1
            
            return True
            
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            
        node_color = {}
        return helper(source)