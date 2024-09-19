class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            arr.extend(row)
        
        arr.sort()

        n = len(arr)

        medians = []
        if n & 1:
            medians.append(arr[n // 2])
        else:
            medians.extend([arr[n // 2 - 1], arr[n // 2]])
        
        min_ops = inf
        ops = 0
        for m in medians:
            for e in arr:
                diff = abs(e - m)
                if diff % x != 0:
                    return -1
                ops += diff // x
            min_ops = min(min_ops, ops)

        return min_ops
