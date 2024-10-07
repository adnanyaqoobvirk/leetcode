class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        s = s + s

        op0 = 0
        op1 = 0
        for i in range(n):
            if s[i] == '0':
                if i & 1:
                    op0 += 1
                else:
                    op1 += 1
            else:
                if i & 1:
                    op1 += 1
                else:
                    op0 += 1
        
        ans = min(op0, op1)
        l = 0
        for r in range(n, len(s)):
            if s[r] == '0':
                if r & 1:
                    op0 += 1
                else:
                    op1 += 1
            else:
                if r & 1:
                    op1 += 1
                else:
                    op0 += 1

            if s[l] == '0':
                if l & 1:
                    op0 -= 1
                else:
                    op1 -= 1
            else:
                if l & 1:
                    op1 -= 1
                else:
                    op0 -= 1
            
            l += 1
            ans = min(ans, op0, op1)
        return ans