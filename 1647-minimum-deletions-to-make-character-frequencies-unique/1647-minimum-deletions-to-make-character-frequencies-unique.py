class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = set()
        deletions = 0
        for _, count in Counter(s).items():
            while count in freqs:
                count -= 1
                deletions += 1
            if count > 0:
                freqs.add(count)
        return deletions