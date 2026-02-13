class Solution:
    def longestBalanced(self, s: str) -> int:
        for guess in reversed(range(1, len(s) + 1)):
            counts = defaultdict(int)
            for i in range(guess):
                counts[s[i]] += 1

            if len(set(counts.values())) == 1:
                return guess
                
            for i in range(guess, len(s)):
                counts[s[i]] += 1
                counts[s[i - guess]] -= 1
                if counts[s[i - guess]] == 0:
                    del counts[s[i - guess]]
                    
                unique_freqs = len(set(counts.values()))
                if unique_freqs == 1:
                    return guess
        return 1