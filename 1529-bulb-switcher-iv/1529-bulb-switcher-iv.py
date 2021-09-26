class Solution:
    def minFlips(self, target: str) -> int:
        current = '0'
        flips = 0
        for bit in target:
            if current != bit:
                flips += 1
                current = '0' if current == '1' else '1'
        return flips