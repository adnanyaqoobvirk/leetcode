class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = bal = 0
        for c in s:
            bal += 1 if c == '(' else -1
            if bal == -1:
                bal += 1
                res += 1
        return bal + res