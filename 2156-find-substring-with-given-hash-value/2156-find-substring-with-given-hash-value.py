class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n, h = len(s), 0
        ans, power_k = n - k, power**k
        for i in reversed(range(n)):
            h = h * power + ord(s[i]) - ord('a') + 1
            if i < n - k:
                h -= (ord(s[i + k]) - ord('a') + 1) * power_k
                if h % modulo == hashValue:
                    ans = i
        return s[ans:ans + k]