class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings.sort()

        column_buildings = defaultdict(list)
        row_buildings = defaultdict(list)

        for i, (x, y) in enumerate(buildings):
            row_buildings[x].append(i)
            column_buildings[y].append(i)
        
        column_candidates = set()
        for column, buildings in column_buildings.items():
            for j in range(1, len(buildings) - 1):
                column_candidates.add(buildings[j])
        
        row_candidates = set()
        for row, buildings in row_buildings.items():
            for j in range(1, len(buildings) - 1):
                row_candidates.add(buildings[j])
        
        return len(row_candidates & column_candidates)