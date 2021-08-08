class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        output = []
        for qx, qy, qr in queries:
            pcount = 0
            for x, y in points:
                d = sqrt((x - qx)**2 + (y - qy)**2)
                if d <= qr:
                    pcount += 1
            output.append(pcount)
        return output