class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i: int, j: int, pos: int) -> bool:
            if pos == k:
                return True
            
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            
            if board[i][j] != word[pos]:
                return False
            
            board[i][j] = '#'
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if helper(a, b, pos + 1):
                    return True
            board[i][j] = word[pos]
            return False
        
        m, n, k = len(board), len(board[0]), len(word)
        
        if k > m * n:
            return False
        
        bcounts = defaultdict(int)
        for row in board:
            for col in row:
                bcounts[col] += 1
        
        for c, count in Counter(word).items():
            if bcounts[c] < count:
                return False
        
        for x in range(m):
            for y in range(n):
                if helper(x, y, 0):
                    return True
        return False