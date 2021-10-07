class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i: int, j: int, pos: int) -> bool:
            if pos == w:
                return True
            
            if 0 > i or i >= n or 0 > j or j >= m or board[i][j] != word[pos]:
                return False
            
            board[i][j] = None
            for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                if backtrack(x, y, pos + 1):
                    return True
            board[i][j] = word[pos]
            
            return False
        
        n, m, w = len(board), len(board[0]), len(word)
        for k in range(n):
            for l in range(m):
                if backtrack(k, l, 0):
                    return True
        return False