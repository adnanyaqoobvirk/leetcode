class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(i: int) -> int:
            if i == n:
                return 1
            
            ans = 0
            for j in range(n):
                diagonal = j - i
                adiagonal = i + j
                if j not in columns and diagonal not in diagonals and adiagonal not in adiagonals:
                    columns.add(j)
                    diagonals.add(diagonal)
                    adiagonals.add(adiagonal)
                    ans += backtrack(i + 1)
                    columns.remove(j)
                    diagonals.remove(diagonal)
                    adiagonals.remove(adiagonal)
            return ans
                      
        columns = set()
        diagonals = set()
        adiagonals = set()
        return backtrack(0)