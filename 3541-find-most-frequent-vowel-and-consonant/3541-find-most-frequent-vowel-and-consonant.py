class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set(list("aeiou"))
        counts = defaultdict(int)
        maxv = 0
        maxc = 0
        for c in s:
            if c in vowels:
                counts[c] += 1
                if counts[c] > maxv:
                    maxv += 1
            else:
                counts[c] += 1
                if counts[c] > maxc:
                    maxc += 1
        return maxv + maxc