class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = [(row[0], i, 1) for i, row in enumerate(matrix)]
        heapify(h)
        
        n, count, k = len(matrix), 0, k - 1
        while count < k:
            _, r, c = heappop(h)
            count = count + 1
            if c < n:
                heappush(h, (matrix[r][c], r, c + 1))
        return h[0][0]
        