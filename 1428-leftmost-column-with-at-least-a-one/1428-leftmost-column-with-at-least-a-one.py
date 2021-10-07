# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        ans = m
        for i in range(n):
            left, right = 0, m
            while left < right:
                mid = left + (right - left) // 2
                if binaryMatrix.get(i, mid):
                    right = mid
                else:
                    left = mid + 1
            ans = min(ans, left)
        return ans if ans != m else -1