class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row_map, col_map, blacks = defaultdict(int), defaultdict(int), []
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B":
                    row_map[i] += 1
                    col_map[j] += 1
                    if row_map[i] == 1 and col_map[j] == 1:
                        blacks.append((i, j))
        
        count = 0
        for i, j in blacks:
            if row_map[i] == 1 and col_map[j] == 1:
                count += 1
        return count