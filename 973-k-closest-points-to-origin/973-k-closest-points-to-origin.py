class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def partition(left: int, right: int, pivot_idx: int) -> int:
            points[pivot_idx], points[right] = points[right], points[pivot_idx]
            
            pivot = left
            for i in range(left, right):
                if points[i][0] <= points[right][0]:
                    points[i], points[pivot] = points[pivot], points[i]
                    pivot += 1
            points[pivot], points[right] = points[right], points[pivot]
            return pivot
        
        def select(left: int, right: int) -> int:
            if left == right:
                return left
            
            pivot = partition(left, right, randint(left, right))
            if pivot == k - 1:
                return pivot
            elif pivot >= k:
                return select(left, pivot - 1)
            else:
                return select(pivot + 1, right)
        points = [(point[0]**2 + point[1]**2, point) for point in points]
        right = select(0, len(points) - 1)
        return [points[i][1] for i in range(right + 1)]
        
        