class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = [amount]
        seen = {amount}
        ans = 0
        while q:
            nq = []
            for r in q:
                if r == 0:
                    return ans
                
                if r > 0:
                    for coin in coins:
                        if r - coin in seen:
                            continue
                        nq.append(r - coin)
                        seen.add(r - coin)
            q = nq
            ans += 1
        return -1