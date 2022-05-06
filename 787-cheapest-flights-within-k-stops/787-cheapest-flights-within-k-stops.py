class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        q, price, prices, count = [src], float('inf'), defaultdict(lambda: float('inf')), 0
        prices[(src, 0)] = 0
        while q and count <= k:
            nq = []
            
            for s in q:
                for d, p in graph[s]:
                    if p + prices[(s, count)] < prices[(d, count + 1)]:
                        if d == dst:
                            price = min(price, p + prices[(s, count)])
                        else:
                            prices[(d, count + 1)] = p + prices[(s, count)]
                            nq.append(d)
            q = nq
            count += 1
        return price if price != float('inf') else -1