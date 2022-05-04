class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dest, cost in pipes:
            graph[src].append((dest, cost))
            graph[dest].append((src, cost))
            
        heap = [(wells[i], i + 1) for i in range(n)]
        heapify(heap)
        
        min_cost, mst = 0, {0}
        while heap:
            cost, dest = heappop(heap)
            
            if dest not in mst:
                min_cost += cost
                mst.add(dest)
                
                for n, c in graph[dest]:
                    if n not in mst:
                        heappush(heap, (c, n))
        return min_cost