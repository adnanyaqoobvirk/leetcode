class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subs = defaultdict(set)

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                
                if v in rows[i]:
                    return False
                rows[i].add(v)
            
                if v in cols[j]:
                    return False
                cols[j].add(v)

                x, y = i // 3, j // 3
                if v in subs[(x, y)]:
                    return False
                subs[(x, y)].add(v)
        
        return True