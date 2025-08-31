class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(row: int, col: int) -> bool:
            if board[row][col] == '.':
                box = (row // sn) * sn + col // sn
                for k in map(str, range(1, 10)):
                    if not (
                        k in row_sets[row] or
                        k in col_sets[col] or 
                        k in sb_sets[box]
                    ):
                        board[row][col] = k
                        row_sets[row].add(k)
                        col_sets[col].add(k)
                        sb_sets[box].add(k)
                        if backtrack(row, col):
                            return True
                        board[row][col] = "."
                        row_sets[row].remove(k)
                        col_sets[col].remove(k)
                        sb_sets[box].remove(k)
            else:
                
                if row == n - 1 and col == n - 1:
                    return True
                
                if col == n - 1:
                    return backtrack(row + 1, 0)
                else:
                    return backtrack(row, col + 1)
            
            return False
        
        n = len(board)
        sn = n // 3
        
        row_sets = [set() for _ in range(n)]
        col_sets = [set() for _ in range(n)]
        sb_sets = [set() for _ in range(n)]
        for row in range(n):
            for col in range(n):
                row_sets[row].add(board[row][col])
                col_sets[col].add(board[row][col])
                sb_sets[(row // sn) * sn + col // sn].add(board[row][col])
                
        backtrack(0, 0)