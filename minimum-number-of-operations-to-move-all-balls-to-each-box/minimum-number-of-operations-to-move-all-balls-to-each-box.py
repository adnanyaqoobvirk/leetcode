class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        iboxes = list(map(int, boxes))
        output = []
        for i in range(len(iboxes)):
            ops = 0
            for j in range(len(iboxes)):
                ops += abs(i - j) * iboxes[j]
            output.append(ops)
        return output