class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [
            (-1, - 1), (-1,  0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                live_count = 0
                for xc, yc in neighbors:
                    x, y = i + xc, j + yc
                    if 0 <= x < m and 0 <= y < n:
                        live_count += board[x][y] % 2
                if board[i][j] % 2:
                    if 2 <= live_count <= 3:
                        board[i][j] = 3
                else:
                    if live_count == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
                    