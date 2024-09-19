class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0
        for c in s:
            if c == 'a':
                a_count += 1
        
        b_count = 0
        min_dels = inf
        for c in s:
            min_dels = min(min_dels, b_count + a_count)

            if c == 'a':
                a_count -= 1
            else:
                b_count += 1
        
        min_dels = min(min_dels, b_count + a_count)
        
        return min_dels
        