class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        if n <= 1:
            return 0
        
        if s[0] != s[-1]:
            for i in range(1, n):
                if s[i] == s[i - 1]:
                    s = s[i:n] + s[:i]
                    break
        
        ops = 0
        pre = "0"
        for cur in s:
            if cur == pre:
                ops += 1
                pre = "0" if cur == "1" else "1"
            else:
                pre = cur

        ans = ops
        pre = "1"
        ops = 0
        for cur in s:
            if cur == pre:
                ops += 1
                pre = "0" if cur == "1" else "1"
            else:
                pre = cur

        return min(ans, ops)