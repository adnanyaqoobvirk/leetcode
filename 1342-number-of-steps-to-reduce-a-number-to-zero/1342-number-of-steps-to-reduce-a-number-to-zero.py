class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        
        steps = 1
        while num > 1:
            if num & 1:
                steps += 1
            num //= 2
            steps += 1
        return steps