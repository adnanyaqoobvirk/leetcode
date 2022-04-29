class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes, colors = {i for i in range(len(graph))}, {}
        while nodes:
            q, blue = [nodes.pop()], True
            while q:
                nq = []
                for curr in q:
                    colors[curr] = blue
                    nodes.discard(curr)
                    
                    for node in graph[curr]:
                        if node not in colors:
                            nq.append(node)
                        else:
                            if colors[node] == blue:
                                return False
                blue = not blue
                q = nq
        return True