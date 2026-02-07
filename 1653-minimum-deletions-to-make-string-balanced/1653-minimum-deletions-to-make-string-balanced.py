class Solution:
    def minimumDeletions(self, s: str) -> int:
        min_dels = 0
        b_count = 0
        for i in range(len(s)):
            if s[i] == 'a':
                min_dels = min(min_dels + 1, b_count)
            else:
                b_count += 1
        return min_dels