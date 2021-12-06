class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = odds = 0
        for p in position:
            if p & 1:
                odds += 1
            else:
                evens += 1
        return min(evens, odds)