class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(i: int, j: int) -> bool:
            if board[i][j] == '.':
                b = (i // 3) * 3 + j // 3
                for k in range(1, 10):
                    k = str(k)
                    if k not in row_sets[i] and k not in col_sets[j] and k not in sb_sets[b]:
                        board[i][j] = k
                        row_sets[i].add(k)
                        col_sets[j].add(k)
                        sb_sets[b].add(k)
                        if backtrack(i, j):
                            return True
                        board[i][j] = "."
                        row_sets[i].remove(k)
                        col_sets[j].remove(k)
                        sb_sets[b].remove(k)
            else:
                if i == 8 and j == 8:
                    return True
                
                if j == 8:
                    return backtrack(i + 1, 0)
                else:
                    return backtrack(i, j + 1)
            return False
        
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        sb_sets = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                row_sets[i].add(board[i][j])
                col_sets[j].add(board[i][j])
                sb_sets[(i // 3) * 3 + j // 3].add(board[i][j])
        backtrack(0, 0)