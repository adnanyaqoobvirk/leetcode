class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def possible(guess: int) -> bool:
            count = 0
            for q in quantities:
                count += math.ceil(q / guess)
                if count > n:
                    return False
            return True

        m = len(quantities)
        lo, hi = 1, max(quantities)
        while lo < hi:
            guess = lo + (hi - lo) // 2
            if possible(guess):
                hi = guess
            else:
                lo = guess + 1
        return hi