class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        if len(position) <= 1:
            return 0
        
        mincost = float('inf')
        for i in range(1, min(len(position), 100) + 1):
            cost = 0
            for j in position:
                c = abs(j - i)
                if c & 1:
                    cost += 1
            mincost = min(mincost, cost)
        return mincost