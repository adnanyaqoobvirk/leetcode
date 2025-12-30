class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(x: int, y: int) -> bool:
            distincts = set()
            main_diagonal_sum = 0
            secondary_diagonal_sum = 0
            col_sums = [0] * 3
            for a in range(x, x + 3):
                row_sum = 0
                for b in range(y, y + 3):
                    v = grid[a][b]
                    if v > 9:
                        return False
                    
                    if v in distincts:
                        return False

                    distincts.add(v)

                    row_sum += v
                    col_sums[b - y] += v

                    if (a - x) - (b - y) == 0:
                        main_diagonal_sum += v

                    if (a - x) + (b - y) == 2:
                        secondary_diagonal_sum += v
                
                if row_sum != target_sum:
                    return False

            for col_sum in col_sums:
                if col_sum != target_sum:
                    return False

            if main_diagonal_sum != target_sum:
                return False
            
            if secondary_diagonal_sum != target_sum:
                return False
            
            return True
        
        m, n = len(grid), len(grid[0])
        target_sum = 15
        magic_square_count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if isMagicSquare(i, j):
                    magic_square_count += 1

        return magic_square_count