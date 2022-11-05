class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i: int, j: int, pos: int) -> bool:
            if pos == k:
                return True
            
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            
            if (i, j) in seen or board[i][j] != word[pos]:
                return False
            
            seen.add((i, j))
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if helper(a, b, pos + 1):
                    return True
            seen.remove((i, j))
            return False
        
        m, n, k = len(board), len(board[0]), len(word)
        for x in range(m):
            for y in range(n):
                seen = set()
                if helper(x, y, 0):
                    return True
        return False