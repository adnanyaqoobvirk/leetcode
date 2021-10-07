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
        j = m - 1
        for i in range(n):
            if j >= 0 and binaryMatrix.get(i, j):
                left, right = 0, j + 1
                while left < right:
                    mid = left + (right - left) // 2
                    if binaryMatrix.get(i, mid):
                        right = mid
                    else:
                        left = mid + 1
                j = left - 1
        return j + 1 if j != m - 1 else -1