class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        minRound, maxRound = math.inf, -math.inf
        @cache
        def dfs(deadMask, i, j, curRound):
            nonlocal minRound, maxRound
            
            if i >= j: # end of round, no more fight possible
                dfs(deadMask, 1, n, curRound + 1)
            
            elif deadMask & (1<<i): # 'i' is dead warrior, try next
                dfs(deadMask, i+1, j, curRound)
        
            elif deadMask & (1<<j): # 'j' is dead warrior, try next
                dfs(deadMask, i, j-1, curRound)
            
            elif i == firstPlayer and j == secondPlayer: # BATTLE OF THE IMMORTALS
                minRound = min(curRound,minRound)
                maxRound = max(curRound,maxRound)
            
            else: # Proceed with a BATTLE with a mortal  
                if i != firstPlayer and i != secondPlayer: # 'i' is MORTAL, he may die
                    dfs(deadMask | (1<<i), i+1, j-1, curRound)
                if j != firstPlayer and j != secondPlayer: # 'j' is MORTAL, he may die
                    dfs(deadMask | (1<<j), i+1, j-1, curRound)
                    
        dfs(0,1,n,1)
        return minRound, maxRound