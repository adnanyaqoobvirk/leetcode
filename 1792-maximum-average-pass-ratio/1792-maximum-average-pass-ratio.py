class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [(-(x + 1)/(y + 1) + x/y, x, y) for x, y in classes if x != y]
        heapify(h)
        for _ in range(extraStudents):
            r, x, y = heappop(h)
            heappush(h, (-(x + 2)/(y + 2) + (x + 1)/(y + 1), x + 1, y + 1))
        return (sum(x/y for _, x, y in h) + len(classes) - len(h)) / len(classes)
