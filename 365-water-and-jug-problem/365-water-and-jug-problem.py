class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        q, seen = [(0, 0)], {(0, 0)}
        while q:
            nq = []
            for a, b in q:
                if a + b == targetCapacity:
                    return True
                
                options = [
                    (jug1Capacity, b),
                    (a, jug2Capacity),
                    (0, b),
                    (a, 0),
                    (max(a - (jug2Capacity - b), 0), min(jug2Capacity, b + a)),
                    (min(jug1Capacity, a + b), max(b - (jug1Capacity - a), 0))
                ]
                
                for t in options:
                    if t not in seen:
                        seen.add(t)
                        nq.append(t)
            q = nq
        return False