class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        parts = []
        start = 0
        end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                parts.append(end - start + 1)
                start = end + 1
        return parts