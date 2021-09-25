class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n, m = len(board), len(board[0])
        while True:
            stable = True
            
            for i in range(n):
                for j in range(m):
                    if i < (n - 2) and abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]) > 0:
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
                        stable = False
                    if j < (m - 2) and abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]) > 0:
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
                        stable = False
            
            for j in range(m):
                p = n - 1
                for i in range(n - 1, -1, -1):
                    if board[i][j] > 0:
                        board[p][j] = board[i][j]
                        p -= 1
                for i in range(p, -1, -1):
                    board[i][j] = 0

            if stable:
                return board
            
            
            