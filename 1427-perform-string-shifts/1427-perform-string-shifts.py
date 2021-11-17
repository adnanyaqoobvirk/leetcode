class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        ops = sum(-amount if direction else amount for direction, amount in shift)
        ops %= len(s)
        return s[ops:] + s[:ops]