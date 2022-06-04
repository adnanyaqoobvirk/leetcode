class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int) -> None:
            if row == n:
                solutions.append(["".join(r) for r in board])
            else:
                for col in range(n):
                    if (
                        col not in cols and 
                        row - col not in diags and 
                        row + col not in adiags
                    ):
                        cols.add(col)
                        diags.add(row - col)
                        adiags.add(row + col)
                            
                        board[row][col] = 'Q'
                        backtrack(row + 1)
                        board[row][col] = '.'
                        
                        cols.remove(col)
                        diags.remove(row - col)
                        adiags.remove(row + col)
                            
        solutions, cols, diags, adiags = [], set(), set(), set()
        board = [['.'] * n for _ in range(n)]
        backtrack(0)
        return solutions