class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        column_buildings = defaultdict(list)
        row_buildings = defaultdict(list)

        for i, (x, y) in enumerate(buildings):
            row_buildings[x].append(i)
            column_buildings[y].append(i)
        
        column_candidates = set()
        for _, candidates in column_buildings.items():
            if len(candidates) < 3:
                continue

            min_row, max_row = inf, -inf
            for j in range(len(candidates)):
                i = candidates[j]
                x = buildings[i][0]
                column_candidates.add(x)
                min_row = min(min_row, x)
                max_row = max(max_row, x)
            column_candidates.discard(min_row)
            column_candidates.discard(max_row)
        
        row_candidates = set()
        for _, candidates in row_buildings.items():
            if len(candidates) < 3:
                continue

            min_col, max_col = inf, -inf
            for j in range(len(candidates)):
                i = candidates[j]
                y = buildings[i][1]
                row_candidates.add(y)
                min_col = min(min_col, y)
                max_col = max(max_col, y)
            row_candidates.discard(min_col)
            row_candidates.discard(max_col)

        return len(row_candidates & column_candidates)