class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(num: int, p: int) -> bool:
            if p > 14 or num < 0:
                return False
            
            if num == 0:
                return True

            if backtrack(num, p + 1):
                return True

            num -= 3**p
            if backtrack(num, p + 1):
                return True
            
            return False

        return backtrack(n, 0)
