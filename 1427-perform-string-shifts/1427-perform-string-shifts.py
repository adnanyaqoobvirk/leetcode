class Solution:
    def stringShift(self, s: str, shift: list[list[int]]) -> str:
        diff = 0
        for d, a in shift:
            if d == 0:
                diff += a
            else:
                diff -= a
        
        diff = diff % len(s)

        if diff < 0:
            return s[len(s) + diff - 1:] + s[: len(s) + diff - 1]
        else:
            return s[diff:] + s[:diff]