class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        
        ships = 0
        for i in range(n):
            for j in range(m):
                if (
                    board[i][j] == 'X'
                    and
                    (not (i < n - 1 and board[i + 1][j] == 'X'))
                    and
                    (not (j < m - 1 and board[i][j + 1] == 'X'))
                ):
                    ships += 1
        return ships