class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        diff = 0
        for d, a in shift:
            diff += a if d else -a
        mid = len(s) - (diff % len(s))
        return s[mid:] + s[:mid]