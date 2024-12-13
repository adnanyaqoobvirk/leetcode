class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def valid(l: int) -> bool:
            if l == 0:
                return True

            count = 0
            for r in ribbons:
                count += r // l
                if count >= k:
                    return True
            return False

        lo, hi = 0, max(ribbons) + 1
        while lo + 1 < hi:
            guess = lo + (hi - lo) // 2

            if valid(guess):
                lo = guess
            else:
                hi = guess
        return lo