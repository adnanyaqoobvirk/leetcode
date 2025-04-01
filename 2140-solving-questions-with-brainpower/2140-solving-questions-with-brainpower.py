class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i: int) -> int:
            if i >= n:
                return 0
            
            return max(dp(i + 1), questions[i][0] + dp(i + questions[i][1] + 1))
        n = len(questions)
        return dp(0)