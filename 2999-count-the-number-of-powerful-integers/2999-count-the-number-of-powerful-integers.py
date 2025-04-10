class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def dfs(v: int, p: int) -> int:
            if v > finish or p > finish:
                return 1 if start <= v <= finish else 0
            ans = 0
            for d in range(limit + 1):
                ans += dfs(v + d * p, p * 10)
            return ans
        return dfs(int(s), 10**len(s))