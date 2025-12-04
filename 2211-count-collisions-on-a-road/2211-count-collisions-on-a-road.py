class Solution:
    def countCollisions(self, directions: str) -> int:
        rcount = 0
        stop = False
        collisions = 0
        for d in directions:
            if d == "R":
                rcount += 1
            elif d == "S":
                collisions += rcount
                stop = True
                rcount = 0
            else:
                if rcount > 0:
                    collisions += rcount + 1
                    rcount = 0
                    stop = True
                elif stop:
                    collisions += 1
        return collisions
