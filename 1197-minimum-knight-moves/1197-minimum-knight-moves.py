class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        possible_moves = [
            (-2, 1), (-2, -1),
            (-1, 2), (-1, -2),
            (1, 2), (1, -2),
            (2, 1), (2, -1)
        ]
        
        start_seen, end_seen = {(0, 0): 0}, {(x, y): 0}
        q = [(0, 0, 0, False), (x, y, 0, True)]
        while q:
            nq = []
            for i, j, steps, end in q:
                if end:
                    if (i, j) in start_seen:
                        return start_seen[(i, j)] + steps
                else:
                    if (i, j) in end_seen:
                        return end_seen[(i, j)] + steps
                
                for a, b in possible_moves:
                    a, b = a + i, b + j
                    if end:
                        if (a, b) not in end_seen:
                            nq.append((a, b, steps + 1, end))
                            end_seen[(a, b)] = steps + 1
                    else:
                        if (a, b) not in start_seen:
                            nq.append((a, b, steps + 1, end))
                            start_seen[(a, b)] = steps + 1
            q = nq
        return -1