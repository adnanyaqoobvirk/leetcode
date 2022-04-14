# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        lo, hi = 0, 10**4 - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            res = reader.get(mid)
            if res == target:
                return mid
            elif res > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1