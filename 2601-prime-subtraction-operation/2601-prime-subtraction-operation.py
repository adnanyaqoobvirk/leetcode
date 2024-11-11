class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def getPrimes(n: int) -> List[int]:
            primes = [True] * n
            p = 2
            while p * p <= n:
                if primes[p]:
                    for i in range(p * p, n, p):
                        primes[i] = False
                p += 1
            return [p for p in range(2, len(primes)) if primes[p]]
        n = max(nums) + 1
        primes = [0] + getPrimes(n)
        prev = 0
        for num in nums:
            i = bisect_right(primes, num - prev)
            curr = num - primes[i - 1]
            if curr <= prev:
                if num <= prev:
                    return False
                else:
                    curr = num
            prev = curr
        return True