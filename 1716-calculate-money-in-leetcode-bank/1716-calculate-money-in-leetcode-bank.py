class Solution:
    def totalMoney(self, n: int) -> int:
        d, r = divmod(n, 7)

        ans = 0
        for i in range(d):
            ans += 7 * (2 * i + 8) // 2
        
        for i in range(r):
            ans += d + 1 + i
        
        return ans