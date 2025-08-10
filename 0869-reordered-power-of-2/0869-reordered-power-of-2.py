class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def backtrack(num: int, pos: int) -> bool:
            if pos == dl:
                return num & (num - 1) == 0
            
            for d in digits:
                if d == 0 and pos == 0:
                    continue

                if digits[d] > 0:
                    digits[d] -= 1
                    if backtrack(num * 10 + d, pos + 1):
                        return True
                    digits[d] += 1
            return False

        digits = defaultdict(int)
        dl = 0
        while n > 0:
            n, r = divmod(n, 10)
            digits[r] += 1
            dl += 1
        return backtrack(0, 0)