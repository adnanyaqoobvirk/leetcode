class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                fives -= 1
                if fives < 0:
                    return False
            else:
                if tens > 0:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
                    
                if tens < 0 or fives < 0:
                    return False
        return True