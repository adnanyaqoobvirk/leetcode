class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def helper(i: int, k: int) -> bool:
            if i == last:
                return True
            
            nk = stones[i] + k 
            
            p1 = helper(vmap[nk - 1], k - 1) if vmap.get(nk - 1, -1) > i else False
            p2 = helper(vmap[nk], k) if vmap.get(nk, -1) > i else False
            p3 = helper(vmap[nk + 1], k + 1) if vmap.get(nk + 1, -1) > i else False
            
            return p1 or p2 or p3
        
        last = len(stones) - 1
        vmap = {v: i for i, v in enumerate(stones)}
        return helper(0, 0)