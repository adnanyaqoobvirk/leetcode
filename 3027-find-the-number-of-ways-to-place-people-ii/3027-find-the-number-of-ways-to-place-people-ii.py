class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        for l in range(n):
            lx, ly = points[l]
            ymax = -inf
            for r in range(l + 1, n):
                rx, ry = points[r]
                if ry > ly:
                    continue
                
                if ry > ymax:
                    count += 1

                ymax = max(ymax, ry)
        return count

