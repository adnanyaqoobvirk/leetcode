class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def backtrack(i: int, t: int) -> int:
            if i == n:
                return t
            
            if accounts[i] <= 0:
                return backtrack(i + 1, t)
            
            ans = inf
            for j in range(n):
                if j != i and accounts[j] < 0:
                    diff = min(-accounts[j], accounts[i])
                    accounts[j] += diff
                    accounts[i] -= diff
                    ans = min(ans, backtrack(i, t + 1))
                    accounts[j] -= diff
                    accounts[i] += diff
            return ans
                    
        accounts, n = defaultdict(int), 0
        for fr, to, am in transactions:
            accounts[fr] -= am
            accounts[to] += am
            n = max(n, fr, to)
        n = n + 1
        return backtrack(0, 0)