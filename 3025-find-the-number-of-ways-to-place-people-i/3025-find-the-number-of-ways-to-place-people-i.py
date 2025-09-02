class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue

                x2, y2 = points[j]
                if x2 < x1 or y2 > y1:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    x3, y3 = points[k]
                    if x1 <= x3 <= x2 and y2 <= y3 <= y1:
                        break
                else:
                    count += 1
        return count