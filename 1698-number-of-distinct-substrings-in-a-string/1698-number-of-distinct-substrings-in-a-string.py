class Solution:
    def countDistinct(self, s: str) -> int:
        P1, M1 = 127, 10**9 + 7
        P2, M2 = 131, 10**9 + 9
        n = len(s)
        ans = 0
        seen1, seen2 = set(), set()
        for i in range(n):
            h1 = h2 = 0
            for j in range(i, n):
                h1 = (h1 * P1 + ord(s[j])) % M1
                h2 = (h2 * P2 + ord(s[j])) % M2
                if h1 in seen1 and h2 in seen2:
                    continue
                seen1.add(h1)
                seen2.add(h2)
                ans += 1
        return ans