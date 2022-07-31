class Solution:
    def addToArrayForm(self, num1: List[int], k: int) -> List[int]:
        num2 = []
        while k > 0:
            k, d = divmod(k, 10)
            num2.append(d)
        num2.reverse()
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1
            
        ans = [0] * (len(num1) + len(num2))
        j = len(num2) - 1
        a = len(ans) - 1
        carry = 0
        for i in reversed(range(len(num1))):
            total = num1[i] + carry
            if j >= 0:
                total += num2[j]
                j -= 1
            carry, d = divmod(total, 10)
            ans[a] = d
            a -= 1
        
        if carry > 0:
            ans[a] = carry
        
        res = []
        leading = True
        for d in ans:
            if not leading or d > 0:
                leading = False
                res.append(d)
        return res
        
            