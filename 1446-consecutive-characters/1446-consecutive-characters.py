class Solution:
    def maxPower(self, s: str) -> int:
        max_power, power, prev_char = 0, 0, ""
        for c in s:
            if c == prev_char:
                power += 1
            else:
                prev_char, power = c, 1
            max_power = max(max_power, power)
        return max_power