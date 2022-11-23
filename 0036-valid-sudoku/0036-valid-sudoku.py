class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                
                if v == '.':
                    continue
                
                if v in row_set[i]:
                    return False
                row_set[i].add(v)
                
                if v in col_set[j]:
                    return False
                col_set[j].add(v)
                
                box = (math.ceil(i // 3) - 1, math.ceil(j // 3) - 1)
                if v in box_set[box]:
                    return False
                box_set[box].add(v)
                
        return True
                
                