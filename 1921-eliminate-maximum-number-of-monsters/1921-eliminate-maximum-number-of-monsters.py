class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        t = [math.ceil(dist[i] / speed[i]) for i in range(len(dist))]
        t.sort()
        
        for i in range(1, len(dist)):
            if t[i] - i <= 0:
                return i
        
        return len(dist)