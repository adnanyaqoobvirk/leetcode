class Solution:
    def numSquares(self, n: int) -> int:
        squares = [
            p * p for p in reversed(range(int(math.sqrt(n)) + 1))
        ]
        
        q = {n}
        level = 0
        while q:
            nq = set()
            for r in q:
                if r == 0:
                    return level
                
                for s in squares:
                    d = r - s
                    if d >= 0:
                        nq.add(d)
            q = nq
            level += 1