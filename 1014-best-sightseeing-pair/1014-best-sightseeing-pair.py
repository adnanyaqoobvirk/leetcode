class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        @cache
        def helper(pos: int, picked: bool) -> int:
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
                    helper(pos + 1, False),
                    values[pos] + pos + helper(pos + 1, True)
                )
        
        n = len(values)
        return helper(0, False)