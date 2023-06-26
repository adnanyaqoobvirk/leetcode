class Solution:
    def countElements(self, arr: List[int]) -> int:
        freq, count = defaultdict(int), 0
        for x in arr:
            freq[x] += 1
            if freq[x + 1] > 0:
                count += 1
            if freq[x] == 1:
                count += freq[x - 1]
        return count