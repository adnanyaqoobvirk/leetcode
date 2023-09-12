class Solution:
    def minDeletions(self, s: str) -> int:
        res, unique_counts = 0, set()
        for count in Counter(s).values():
            while count in unique_counts:
                count -= 1
                res += 1
            if count != 0:
                unique_counts.add(count)
        return res