class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        
        UF = {i: i for i in range(n)}
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF[find(x)] = find(y)
            
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        
        return n - len({find(i) for i in range(n)})