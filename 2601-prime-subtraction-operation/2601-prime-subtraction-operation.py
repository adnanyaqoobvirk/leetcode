class Solution:
    def __init__(self):
        n = 1001
        primes = [True] * n
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n, p):
                    primes[i] = False
            p += 1
        
        p = 0
        for i in range(n):
            if primes[i]:
                primes[i] = p
                p = i
            else:
                primes[i] = p

        self.primes = primes

    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = 0
        for num in nums:
            p = self.primes[num - prev]
            curr = num - p
            if curr <= prev:
                if num <= prev:
                    return False
                else:
                    curr = num
            prev = curr
        return True