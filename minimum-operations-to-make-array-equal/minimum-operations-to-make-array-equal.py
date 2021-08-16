class Solution:
    def minOperations(self, n: int) -> int:
        ops = 0
        start = 0
        end = n - 1
        while start < end:
            ops += ((2 * end + 1) - (2 * start + 1)) // 2
            start += 1
            end -= 1
        return ops