class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        @cache
        def recurse(pos: int, time: int) -> int:
            if pos == n:
                return 0
            
            return max(
                satisfaction[pos] * time + recurse(pos + 1, time + 1),
                recurse(pos + 1, time)
            )
        
        n = len(satisfaction)
        satisfaction.sort()
        return recurse(0, 1)