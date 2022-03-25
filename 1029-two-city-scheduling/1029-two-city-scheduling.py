class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @cache
        def helper(i: int, acount: int, bcount: int) -> int:
            if i >= twon:
                return 0
            
            return min(
                costs[i][0] + helper(i + 1, acount + 1, bcount) if acount < n else costs[i][1] + helper(i + 1, acount, bcount + 1) ,
                costs[i][1] + helper(i + 1, acount, bcount + 1) if bcount < n else costs[i][0] + helper(i + 1, acount + 1, bcount)
            )
    
        twon = len(costs)
        n = twon // 2
        return helper(0, 0, 0)