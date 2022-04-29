class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes, colors = {i for i in range(len(graph))}, {}
        while nodes:
            stack = [(nodes.pop(), True)]
            while stack:
                curr, color = stack.pop()
                colors[curr] = color
                nodes.discard(curr)
                
                for node in graph[curr]:
                    if node not in colors:
                        stack.append((node, not color))
                    else:
                        if colors[node] == color:
                            return False
        return True