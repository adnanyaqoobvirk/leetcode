class Solution:
    def numSquares(self, n: int) -> int:
        squares = [num**2 for num in range(1, int(sqrt(n)) + 1)]
        
        q = {n}
        ans = 0
        while q:
            nq = set()
            for remaining in q:
                if remaining == 0:
                    return ans
                
                for j in range(int(sqrt(remaining))):
                    nr = remaining - squares[j]
                    if nr not in nq:
                        nq.add(nr)
            q = nq
            ans += 1
        return ans