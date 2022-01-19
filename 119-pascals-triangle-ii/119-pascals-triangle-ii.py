class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @cache
        def helper(i: int, j: int) -> int:
            if i == 0 or j == 0 or i == j:
                return 1
            
            return helper(i - 1, j - 1) + helper(i - 1, j)
        
        return [helper(rowIndex, k) for k in range(rowIndex + 1)]