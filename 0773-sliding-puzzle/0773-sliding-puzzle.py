class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        target = ((1, 2, 3), (4, 5, 0))
        seen = {(tuple(board[0]), tuple(board[1]))}
        q = [(i, j, next(iter(seen))) for i in range(m) for j in range(n) if board[i][j] == 0]
        moves = 0
        while q:
            nq = []
            for i, j, B in q:
                if B == target:
                    return moves
                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= a < m and 0 <= b < n:
                        NB = [list(row) for row in B]
                        NB[a][b], NB[i][j] = NB[i][j], NB[a][b]
                        NB = (tuple(NB[0]), tuple(NB[1]))
                        if NB not in seen:
                            nq.append((a, b, NB))
                            seen.add(NB)
            q = nq
            moves += 1
        return -1
        