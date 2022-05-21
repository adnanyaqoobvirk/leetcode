class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q, seen, deadends, moves = ["0000"], {"0000"}, set(deadends), 0
        while q:
            nq = []
            for comb in q:
                if comb in deadends:
                    continue
                    
                if comb == target:
                    return moves
                
                for i in range(4):
                    for move in [-1, 1]:
                        ncomb = f"{comb[0:i]}{(int(comb[i]) + move) % 10}{comb[i+1:]}"
                        if ncomb not in seen:
                            seen.add(ncomb)
                            nq.append(ncomb)
            q = nq
            moves += 1
        return -1