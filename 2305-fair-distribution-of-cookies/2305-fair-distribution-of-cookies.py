class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(pos: int) -> int:
            if pos == n:
                return max(distribution)
            
            min_unfairness = inf
            for child in range(k):
                if distribution[child] + cookies[pos] > max_allowed_cookies:
                    continue
                    
                distribution[child] += cookies[pos]
                min_unfairness = min(
                    min_unfairness,
                    backtrack(pos + 1)
                )
                distribution[child] -= cookies[pos]
            return min_unfairness
        n = len(cookies)
        max_allowed_cookies = sum(sorted(cookies, reverse=True)[:ceil(n/k)])
        distribution = [0] * k
        return backtrack(0)