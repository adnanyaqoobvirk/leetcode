class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dp(i: int, x: int, y: int) -> int:
            if x < 0 or y < 0:
                return -inf
            
            if i >= l:
                return 0
            
            return max(1 + dp(i + 1, x - counts[i][0], y - counts[i][1]), dp(i + 1, x, y))
        
        l = len(strs)
        counts = []
        for s in strs:
            cnt = Counter(s)
            counts.append([cnt["0"], cnt["1"]])
        
        return dp(0, m, n)
            
