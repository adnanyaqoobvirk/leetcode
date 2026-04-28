class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            arr.extend(row)
        arr.sort()

        m = arr[len(arr) // 2]
        ops = 0
        for e in arr:
            diff = abs(e - m)
            if diff % x != 0:
                return -1
            ops += diff // x
        return ops
