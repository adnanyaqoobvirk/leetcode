class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        @cache
        def recurse(i: int, j: int) -> int:
            if i > n or j > m:
                return float('inf')
            
            if i == n and j == m:
                return -dungeon[i][j] + 1 if dungeon[i][j] < 0 else 1
            
            health = min(
                recurse(i + 1, j),
                recurse(i, j + 1)
            ) - dungeon[i][j]
            
            return 1 if health <= 0 else health 
        
        n, m = len(dungeon) - 1, len(dungeon[0]) - 1
        return recurse(0, 0)