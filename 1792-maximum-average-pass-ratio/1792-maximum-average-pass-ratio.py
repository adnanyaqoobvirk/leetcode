class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [(-(p + 1) / (t + 1) + p / t , p, t) for p, t in classes]
        heapify(h)

        for _ in range(extraStudents):
            pr, p, t = heappop(h)
            p += 1
            t += 1
            heappush(h, (-(p + 1) / (t + 1) + p / t, p, t))

        tavg = 0
        for _, p, t in h:
            tavg += p / t
        return tavg / len(classes)