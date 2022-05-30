class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_count = 0
        q, seen = [amount], {amount}
        while q:
            nq = []
            for r in q:
                if r == 0:
                    return coin_count
                for coin in coins:
                    nr = r - coin
                    if nr >= 0 and nr not in seen:
                        nq.append(nr)
                        seen.add(nr)
            q = nq
            coin_count += 1
        return -1