class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n > 1:
            total = 0
            while n > 0:
                n, d = divmod(n, 10)
                total += d * d
                
            if total in seen:
                return False
            seen.add(total)
            
            n = total
        return True