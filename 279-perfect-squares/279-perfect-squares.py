class Solution:
    def numSquares(self, n: int) -> int:
        squares = [num**2 for num in range(1, int(sqrt(n)) + 1)]
        
        q = [n]
        seen = {n}
        ans = 0
        while q:
            nq = []
            for remaining in q:
                if remaining == 0:
                    return ans
                
                for square in squares:
                    if remaining - square < 0:
                        break
                    if remaining - square not in seen:
                        seen.add(remaining - square)
                        nq.append(remaining - square)
            q = nq
            ans += 1
        return ans