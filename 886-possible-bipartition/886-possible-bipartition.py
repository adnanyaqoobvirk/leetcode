class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for src, dst in dislikes:
            graph[src].append(dst)
            graph[dst].append(src)
            
        colors = defaultdict(bool)
        nodes = {node for node in range(n)}
        while nodes:
            q, blue = [nodes.pop()], True
            while q:
                nq = []
                for src in q:
                    colors[src] = blue
                    for dst in graph[src]:
                        if dst in colors:
                            if colors[dst] == blue:
                                return False
                        else:
                            nodes.discard(dst)
                            nq.append(dst)
                q = nq
                blue = not blue
        return True