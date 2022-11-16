class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = 0
        while n > coins:
            coins += 1
            n -= coins
        return coins