class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        heap, node_prices = [(0, 0, src)], defaultdict(lambda: (float('inf'), float('inf')))
        node_prices[src] = (0, 0)
        while heap:
            price, stops, s = heappop(heap)
            
            if s == dst:
                break
            
            if stops <= k:
                for d, p in graph[s]:
                    if price + p < node_prices[d][0]:
                        node_prices[d] = (price + p, stops + 1)
                        heappush(heap, (price + p, stops + 1, d))
                    elif stops <= node_prices[d][1]:
                        heappush(heap, (price + p, stops + 1, d))
        return node_prices[dst][0] if dst in node_prices else -1