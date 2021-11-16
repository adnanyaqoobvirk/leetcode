class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        count = total = 0
        for w in sorted(weight):
            total += w
            if total > 5000:
                break
            count += 1
        return count