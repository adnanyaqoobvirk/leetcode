class Solution:
    def __init__(self):
        n = 1001
        primes = [True] * n
        primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n, p):
                    primes[i] = False
            p += 1
        self.primes = [p for p in range(len(primes)) if primes[p]]

    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = self.primes
        prev = 0
        for num in nums:
            i = bisect_left(primes, num - prev)
            curr = num - primes[max(i - 1, 0)]
            if curr <= prev:
                if num <= prev:
                    return False
                else:
                    curr = num
            prev = curr
        return True