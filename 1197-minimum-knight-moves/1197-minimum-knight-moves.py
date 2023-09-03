class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (2, -1),
            (2, 1), (1, 2)
        ]
        
        seen, q, steps = {(0, 0)}, [(0, 0)], 0
        while q:
            nq = []
            for i, j in q:
                if i == x and j == y:
                    return steps
                
                for di, dj in moves:
                    xy = (i + di, j + dj)
                    
                    if xy not in seen:
                        nq.append(xy)
                        seen.add(xy)
            q = nq
            steps += 1
        return -1