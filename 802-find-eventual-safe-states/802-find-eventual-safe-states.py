class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def helper(curr: int) -> bool:
            if color[curr] == GREY:
                return False
            
            if color[curr] == BLACK:
                return True
            
            color[curr] = GREY
            for neighbor in graph[curr]:
                if not helper(neighbor):
                    safe_nodes.discard(curr)
                    return False
            color[curr] = BLACK
            
            return True
        
        WHITE, GREY, BLACK = 0, 1, 2
        safe_nodes, color = {node for node in range(len(graph))}, defaultdict(int)
        for node in range(len(graph)):
            if color[node] == WHITE:
                helper(node)
        return sorted(safe_nodes)