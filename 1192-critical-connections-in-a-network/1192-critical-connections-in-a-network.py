class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def helper(src: int, rank: int) -> int:
            if nodes[src] != -1:
                return nodes[src]
            
            nodes[src], min_rank = rank, rank + 1
            for dst in graph[src]:
                if nodes[dst] != -1 and nodes[dst] == (rank - 1):
                    continue
                
                rrank = helper(dst, rank + 1)
                if rrank <= rank:
                    criticals.discard((src, dst))
                    criticals.discard((dst, src))
                    
                min_rank = min(rrank, min_rank)
            return min_rank
        
        graph, criticals = defaultdict(list), set()
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)
            
            criticals.add((src, dst))
        
        nodes = [-1] * n
        helper(0, 0)
        return criticals