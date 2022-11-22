class Solution:
    def numSquares(self, n: int) -> int:
        nsqrt = int(math.sqrt(n)) + 1
        
        q = [n]
        seen = {n}
        ans = 0
        while q:
            nq = []
            for r in q:
                if r == 0:
                    return ans
                
                for p in reversed(range(nsqrt)):
                    d = r - p * p
                    if d >= 0 and d not in seen:
                        seen.add(d)
                        nq.append(d)
            q = nq
            ans += 1
        return ans