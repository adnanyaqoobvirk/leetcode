class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        
        UF = {}
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        for i, j in stones:
            union(i, j + 10001)
        
        return n - len({find(i) for i in UF})