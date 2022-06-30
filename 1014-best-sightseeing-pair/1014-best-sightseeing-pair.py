class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        @cache
        def helper(pos: int, picked: int) -> int:
            if picked and pos == n - 1:
                return values[pos] - pos
            
            if pos == n:
                return -inf
            
            if picked:
                return max(
                    values[pos] - pos,
                    helper(pos + 1, picked)
                )
            else:
                return max(
                    helper(pos + 1, 0),
                    values[pos] + pos + helper(pos + 1, 1)
                )
        
        n = len(values)
        return helper(0, 0)
    
        