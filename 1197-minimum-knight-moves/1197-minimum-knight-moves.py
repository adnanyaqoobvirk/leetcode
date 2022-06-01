class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        possible_moves = [
            (-2, 1), (-2, -1),
            (-1, 2), (-1, -2),
            (1, 2), (1, -2),
            (2, 1), (2, -1)
        ]
        
        x, y = abs(x), abs(y)
        q, moves, seen = [(0, 0)], 0, {(0, 0)}
        while q:
            nq = []
            for i, j in q:
                if i == x and j == y:
                    return moves
                for a, b in possible_moves:
                    ab = abs(a + i), abs(b + j)
                    if ab not in seen:
                        seen.add(ab)
                        nq.append(ab)
            q = nq
            moves += 1
        return -1