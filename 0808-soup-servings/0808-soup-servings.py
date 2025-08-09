class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 10000:
            return 1

        @cache
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0 and b > 0:
                return 1
            if a <= 0 or b <= 0:
                return 0
            
            res = 0
            for da, db in turns:
                res += dp(a - da, b - db)
            return res * 0.25
        turns = [(4, 0), (3, 1), (2, 2), (1, 3)]
        return dp(ceil(n / 25), ceil(n / 25))
