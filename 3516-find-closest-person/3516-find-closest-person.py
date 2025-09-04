class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a, b = abs(x - z), abs(y - z)
        if a == b:
            return 0
        elif a < b:
            return 1
        else:
            return 2