class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        lcount = 0
        rcount = 0
        dcount = 0
        for m in moves:
            if m == "L":
                lcount += 1
            elif m == "R":
                rcount += 1
            else:
                dcount += 1
        return max(dcount + lcount - rcount, dcount + rcount - lcount)