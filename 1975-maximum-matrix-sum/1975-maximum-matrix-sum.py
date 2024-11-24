class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_val = inf
        count = total = 0
        for row in matrix:
            for num in row:
                if num < 0:
                    count += 1
                    total -= num
                else:
                    total += num
                min_val = min(min_val, abs(num))
        return total - (2 * min_val) if count & 1 else total