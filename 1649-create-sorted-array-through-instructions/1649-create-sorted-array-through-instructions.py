from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sl = SortedList()
        cost = 0
        for num in instructions:
            i, j = sl.bisect_left(num), sl.bisect_right(num)
            cost += min(i, len(sl) - j)
            sl.add(num)
        return cost % (10**9 + 7)