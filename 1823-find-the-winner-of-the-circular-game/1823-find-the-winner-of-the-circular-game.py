class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n + 1)]
        loserCount = pos = 0
        while loserCount < n - 1:
            i = 0
            while i < k:
                if friends[pos]:
                    i += 1
                pos += 1
                if pos == n:
                    pos = 0
            loserCount += 1
            friends[pos - 1] = 0
        
        for f in friends:
            if f:
                return f