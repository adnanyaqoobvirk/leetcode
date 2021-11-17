class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = deque()
        
        carry = 0
        for i in range(1, max(len(num1), len(num2)) + 1):
            total = int(num1[-i]) if i <= len(num1) else 0
            if i <= len(num2):
                total += int(num2[-i])
            
            carry, digit = divmod(total + carry, 10)
            ans.appendleft(str(digit))
        
        if carry:
            ans.appendleft(str(carry))
            
        return "".join(ans)