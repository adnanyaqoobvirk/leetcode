class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(i: int, maximum: int, zeros: int):
            if n - i < zeros:
                return inf
            
            if i == n:
                return maximum
            
            m = inf
            for j in range(k):
                childs[j] += cookies[i]
                m = min(m, backtrack(i + 1, max(maximum, childs[j]), zeros - 1 if childs[j] - cookies[i] == 0 else zeros))
                childs[j] -= cookies[i]
            return m
        
        n = len(cookies)
        childs = [0] * k
        return backtrack(0, 0, k)