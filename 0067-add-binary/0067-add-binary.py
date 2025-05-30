class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        p1, p2 = m - 1, n - 1
        c = 0
        ans = []
        while p1 >= 0 or p2 >= 0:
            d1 = 0 if p1 < 0 else int(a[p1])
            d2 = 0 if p2 < 0 else int(b[p2])

            c, d = divmod(d1 + d2 + c, 2)
            ans.append(str(d))
            p1, p2 = p1 - 1, p2 - 1
        if c > 0:
            ans.append("1")
        return "".join(reversed(ans))