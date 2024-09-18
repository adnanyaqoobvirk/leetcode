class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        acount = []
        count = 0
        for i in reversed(range(n)):
            acount.append(count)
            if s[i] == 'a':
                count += 1

        bcount = []
        count = 0
        for i in range(n):
            bcount.append(count)
            if s[i] == 'b':
                count += 1
        
        min_dels = inf
        for i in range(n):
            min_dels = min(min_dels, acount[n - i - 1] + bcount[i])
        
        return min_dels
        