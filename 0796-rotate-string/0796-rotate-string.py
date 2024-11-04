class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)

        if n != len(goal):
            return False

        P1, P2, M1, M2 = 29, 31, 10**9 + 7, 10**9 + 9

        g = goal + goal
        sidx = ord('a') - 1
        phash1 = phash2 = 0
        rhash1 = rhash2 = 0
        p1max = p2max = 1
        for i in range(n):
            cidx = ord(s[i]) - sidx
            phash1 = (phash1 * P1 + cidx) % M1
            phash2 = (phash2 * P2 + cidx) % M2
            
            cidx = ord(g[i]) - sidx
            rhash1 = (rhash1 * P1 + cidx) % M1
            rhash2 = (rhash2 * P2 + cidx) % M2

            p1max = p1max * P1 % M1
            p2max = p2max * P2 % M2
        
        if phash1 == rhash1 and phash2 == rhash2:
            return True
        
        p1max = p1max // P1
        p2max = p2max // P2
        for i in range(n, len(g)):
            c1idx = ord(g[i - n]) - sidx
            c2idx = ord(g[i]) - sidx
            rhash1 = ((rhash1 - (p1max * c1idx)) * P1 + c2idx) % M1
            rhash2 = ((rhash2 - (p2max * c1idx)) * P2 + c2idx) % M2

            if rhash1 == phash1 and rhash2 == phash2:
                return True
        return False
