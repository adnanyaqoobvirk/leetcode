class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        target = tuple(int(c) for c in target)
        visited = set((int(a), int(b), int(c), int(d)) for a, b, c, d in deadends)
        q = [(0,0,0,0,0)]
        while q:
            nq = []
            for a, b, c, d, turns in q:
                t = (a,b,c,d)
                if t == target:
                    return turns
                
                if t in visited:
                    continue
                
                visited.add(t)
                turns += 1
                for diff in [-1, 1]:
                    nq.append(((a + diff) % 10, b, c, d, turns))
                    nq.append((a, (b + diff) % 10, c, d, turns))
                    nq.append((a, b, (c + diff) % 10, d, turns))
                    nq.append((a, b, c, (d + diff) % 10, turns))
            q = nq
        return -1