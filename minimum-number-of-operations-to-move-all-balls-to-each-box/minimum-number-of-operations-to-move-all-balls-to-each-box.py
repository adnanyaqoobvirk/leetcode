class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output_1 = [0] * len(boxes)
        one_count = 0
        for i in range(1, len(boxes)):
            if boxes[i - 1] == '1':
                one_count += 1
            output_1[i] = output_1[i - 1] + one_count
        
        output_2 = [0] * len(boxes)
        one_count = 0
        for i in range(len(boxes) - 2, -1, -1):
            if boxes[i + 1] == '1':
                one_count += 1
            output_2[i] = output_2[i + 1] + one_count
        
        return [output_1[i] + output_2[i] for i in range(len(boxes))]