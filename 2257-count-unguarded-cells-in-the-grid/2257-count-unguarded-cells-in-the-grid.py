class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        seen = set()
        walls = set(tuple(w) for w in walls)
        guards = set(tuple(g) for g in guards)
        for i, j in guards:
            for r in range(i - 1, -1, -1):
                if (r, j) in walls or (r, j) in guards:
                    break
                seen.add((r, j))
            for r in range(i + 1, m):
                if (r, j) in walls or (r, j) in guards:
                    break
                seen.add((r, j))
            for c in range(j - 1, -1, -1):
                if (i, c) in walls or (i, c) in guards:
                    break
                seen.add((i, c))
            for c in range(j + 1, n):
                if (i, c) in walls or (i, c) in guards:
                    break
                seen.add((i, c))
        return m * n - len(walls) - len(seen) - len(guards)