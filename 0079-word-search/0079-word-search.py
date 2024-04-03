class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i: int, j: int, k: int) -> bool:
            if k >= l:
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            
            if board[i][j] != word[k]:
                return False
            
            board[i][j] = "."
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if backtrack(a, b, k + 1):
                    return True
            board[i][j] = word[k]
            
            return False
        
        m, n = len(board), len(board[0])
        l = len(word)
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
                
        return False