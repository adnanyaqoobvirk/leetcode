class Solution:
    def largestVariance(self, s: str) -> int:
        counts = Counter(s)
        chars = list(counts.keys())
        n = len(chars)
        max_var = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                ch1, ch2 = chars[i], chars[j]

                ch1_count = 0
                ch2_count = 0
                ch2_remaining = counts[ch2]
                for c in s:
                    if c == ch1:
                        ch1_count += 1
                    elif c == ch2:
                        ch2_count += 1
                        ch2_remaining -= 1
                    
                    if ch2_count > 0:
                        max_var = max(max_var, ch1_count - ch2_count)
                    
                    if ch2_remaining > 0 and ch1_count < ch2_count:
                        ch1_count = 0
                        ch2_count = 0
        return max_var