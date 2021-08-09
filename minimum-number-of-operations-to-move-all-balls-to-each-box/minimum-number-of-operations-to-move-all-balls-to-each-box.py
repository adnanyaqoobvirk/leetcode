class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        return [
            sum(abs(i - j) for j in range(n) if boxes[j] == '1') 
            for i in range(n)
        ]