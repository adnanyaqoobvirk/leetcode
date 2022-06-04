class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int) -> None:
            if row == n:
                solutions.append(["".join(r) for r in board])
            else:
                for col in range(n):
                    if invalids[(row, col)] <= 0:
                        for i in range(n):
                            invalids[(row, i)] += 1
                            invalids[(i, col)] += 1
                            
                        c = col
                        for r in reversed(range(row)):
                            c += 1
                            invalids[(r, c)] += 1
                        c = col
                        for r in reversed(range(row)):
                            c -= 1
                            invalids[(r, c)] += 1
                            
                        c = col
                        for r in range(row + 1, n):
                            c += 1
                            invalids[(r, c)] += 1
                        c = col
                        for r in range(row + 1, n):
                            c -= 1
                            invalids[(r, c)] += 1
                            
                        board[row][col] = 'Q'
                        backtrack(row + 1)
                        board[row][col] = '.'
                        
                        for i in range(n):
                            invalids[(row, i)] -= 1
                            invalids[(i, col)] -= 1
                            
                        c = col
                        for r in reversed(range(row)):
                            c += 1
                            invalids[(r, c)] -= 1
                        c = col
                        for r in reversed(range(row)):
                            c -= 1
                            invalids[(r, c)] -= 1
                            
                        c = col
                        for r in range(row + 1, n):
                            c += 1
                            invalids[(r, c)] -= 1
                        c = col
                        for r in range(row + 1, n):
                            c -= 1
                            invalids[(r, c)] -= 1
                            
        solutions, invalids = [], defaultdict(int)
        board = [['.'] * n for _ in range(n)]
        backtrack(0)
        return solutions