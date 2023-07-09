class Solution:
    def largestVariance(self, s: str) -> int:
        counts = Counter(s)
        chars = counts.keys()
        
        ans = 0
        for c1 in chars:
            for c2 in chars:
                if c1 == c2:
                    continue
                
                c1_counts, c2_counts, reset = 0, 0, counts[c2]
                for c in s:
                    if c == c1:
                        c1_counts += 1
                    elif c == c2:
                        reset -= 1
                        c2_counts += 1
                    
                    if c2_counts > 0:
                        ans = max(ans, c1_counts - c2_counts)
                        
                    if reset > 0 and c1_counts < c2_counts:
                        c1_counts = c2_counts = 0
        return ans
                    
                