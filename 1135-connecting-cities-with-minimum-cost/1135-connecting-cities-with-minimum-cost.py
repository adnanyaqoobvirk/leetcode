class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y, cost in connections:
            graph[x].append((y, cost))
            graph[y].append((x, cost))
        
        h = [(0, 1)]
        visited = set()
        min_cost = 0
        while h:
            cost, x = heappop(h)
            
            if x in visited:
                continue

            visited.add(x)
            min_cost += cost

            for y, cost in graph[x]:
                if y not in visited:
                    heappush(h, (cost, y))

        if len(visited) == n:
            return min_cost
        
        return -1