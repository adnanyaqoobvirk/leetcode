class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        minutes = 0
        stop = False
        all_rotten = False
        while not stop and not all_rotten:
            all_rotten = True
            stop = True
            any_fresh = False
            ignore = set()
            for i in range(n):
                for j in range(m):
                    if (i, j) not in ignore and grid[i][j] == 2:
                        if i - 1 >= 0 and grid[i - 1][j] == 1:
                            grid[i - 1][j] = 2
                            ignore.add((i - 1, j))
                            any_fresh = True
                        
                        if i + 1 < n and grid[i + 1][j] == 1:
                            grid[i + 1][j] = 2
                            ignore.add((i + 1, j))
                            any_fresh = True
                        
                        if j - 1 >= 0 and grid[i][j - 1] == 1:
                            grid[i][j - 1] = 2
                            ignore.add((i, j - 1))
                            any_fresh = True
                        
                        if j + 1 < m and grid[i][j + 1] == 1:
                            grid[i][j + 1] = 2
                            ignore.add((i, j + 1))
                            any_fresh = True
                        
                        grid[i][j] = -2
                        stop = False
                    elif grid[i][j] == 1:
                        all_rotten = False
            if any_fresh:
                minutes += 1
        return minutes if all_rotten else -1
                            