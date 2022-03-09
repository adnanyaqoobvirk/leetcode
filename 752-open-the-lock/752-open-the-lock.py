class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        target = tuple(int(c) for c in target)
        visited = set((int(a), int(b), int(c), int(d)) for a, b, c, d in deadends)
        q = [(0,0,0,0,0)]
        while q:
            nq = []
            for a, b, c, d, turns in q:
                if (a, b, c, d) == target:
                    return turns
                
                if (a, b, c, d) in visited:
                    continue
                
                visited.add((a, b, c, d))
                for na in [a - 1, a + 1]:
                    na %= 10
                    nq.append((na, b, c, d, turns + 1))
                
                for nb in [b - 1, b + 1]:
                    nb %= 10
                    nq.append((a, nb, c, d, turns + 1))
                    
                for nc in [c - 1, c + 1]:
                    nc %= 10
                    nq.append((a, b, nc, d, turns + 1))
                    
                for nd in [d - 1, d + 1]:
                    nd %= 10
                    nq.append((a, b, c, nd, turns + 1))
            q = nq
        return -1