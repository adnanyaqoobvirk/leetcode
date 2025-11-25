class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        seen = set()
        n = 0
        digits = 0
        while True:
            n = (n * 10 + 1) % k
            digits += 1
            if n == 0:
                return digits
            elif n in seen:
                break
            seen.add(n)
        return -1