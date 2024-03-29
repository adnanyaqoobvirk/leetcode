class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
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
                    ab = (abs(i + di), abs(j + dj))
                    
                    if ab not in seen:
                        nq.append(ab)
                        seen.add(ab)
            q = nq
            steps += 1
        return -1