class Solution:
    def numSquares(self, n: int) -> int:
        squares = [p * p for p in reversed(range(int(math.sqrt(n)) + 1))]
        
        q = [n]
        seen = {n}
        ans = 0
        while q:
            nq = []
            for r in q:
                if r == 0:
                    return ans
                
                for s in squares:
                    d = r - s
                    if d >= 0 and d not in seen:
                        seen.add(d)
                        nq.append(d)
            q = nq
            ans += 1
        return ans