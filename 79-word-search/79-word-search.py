class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i: int, j: int, pos: int) -> bool:
            if pos == w:
                return True
            
            for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and board[x][y] == word[pos]:
                    board[x][y] = None
                    if backtrack(x, y, pos + 1):
                        return True
                    board[x][y] = word[pos]
            return False
        
        n, m, w = len(board), len(board[0]), len(word)
        for k in range(n):
            for l in range(m):
                if board[k][l] == word[0]:
                    board[k][l] = None
                    if backtrack(k, l, 1):
                        return True
                    board[k][l] = word[0]
        return False