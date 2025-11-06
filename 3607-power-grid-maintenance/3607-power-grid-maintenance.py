class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)
        
        stations = set(range(1, c + 1))
        grids = []
        station_map = {}
        while stations:
            q = [stations.pop()]
            grid_id = len(grids)
            grid = SortedSet([q[0]])
            station_map[q[0]] = grid_id
            while q:
                nq = []
                for station in q:
                    for nei in graph[station]:
                        if nei not in grid:
                            nq.append(nei)
                            stations.remove(nei)
                            grid.add(nei)
                            station_map[nei] = grid_id
                q = nq
            grids.append(grid)
        
        ans = []
        for op, station in queries:
            grid_id = station_map[station]
            grid = grid = grids[grid_id]
            if op == 1:
                if station in grid:
                    ans.append(station)
                else:
                    if grid:
                        ans.append(grid[0])
                    else:
                        ans.append(-1)
            else:
                grid.discard(station)
        return ans