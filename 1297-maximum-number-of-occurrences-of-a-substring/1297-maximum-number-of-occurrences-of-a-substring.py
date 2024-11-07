class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        P, M = 127, 10**9 + 7

        hcounts = defaultdict(int)
        uchars = defaultdict(int)
        rhash = 0
        pmax = 1
        for i in range(minSize):
            if i > 0:
                pmax = pmax * P % M
            rhash = (rhash * P + ord(s[i])) % M
            uchars[s[i]] += 1
        
        if len(uchars) <= maxLetters:
            hcounts[rhash] += 1
        
        for i in range(minSize, len(s)):
            prev, curr = s[i - minSize], s[i]
            rhash -= pmax * ord(prev)
            rhash = (rhash * P + ord(curr)) % M

            uchars[prev] -= 1
            if uchars[prev] == 0:
                del uchars[prev]
            uchars[curr] += 1

            if len(uchars) <= maxLetters:
                hcounts[rhash] += 1
        return max(hcounts.values()) if len(hcounts) > 0 else 0




