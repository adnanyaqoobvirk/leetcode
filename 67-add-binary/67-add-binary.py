class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m, ans = len(a), len(b), []
        
        carry, i, j = 0, n - 1, m - 1
        while i >= 0 and j >= 0:
            carry, d = divmod(int(a[i]) + int(b[j]) + carry, 2)
            ans.append(str(d))
            i -= 1
            j -= 1
        
        k, c = (i, a) if i >= 0 else (j, b)
        while k >= 0:
            carry, d = divmod(int(c[k]) + carry, 2)
            ans.append(str(d))
            k -= 1
        
        if carry: ans.append("1")
            
        return "".join(reversed(ans))
        
        