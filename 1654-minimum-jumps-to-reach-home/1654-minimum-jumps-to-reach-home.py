class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        BACKWARD_ALLOWED, BACKWARD_NOT_ALLOWED = 0, 1
        MIN_INDEX, MAX_INDEX = 0, a + b + max(x, max(forbidden))
        
        seen, forbidden = set(), set(forbidden)
        jumps, q = 0, [(0, BACKWARD_NOT_ALLOWED)]
        while q:
            nq = []
            for i, status in q:
                if i == x:
                    return jumps
                
                if (
                    MIN_INDEX <= i <= MAX_INDEX and
                    i not in forbidden and
                    (i, status) not in seen
                ):
                    seen.add((i, status))
                    nq.append((i + a, BACKWARD_ALLOWED))
                    if status == BACKWARD_ALLOWED:
                        nq.append((i - b, BACKWARD_NOT_ALLOWED))
            jumps += 1
            q = nq
        return -1
            