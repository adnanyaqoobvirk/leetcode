class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        
        ones = 0
        ops = 0
        for i in range(n):
            ops += ones
            if boxes[i] == "1":
                ones += 1
            ans[i] += ops
        
        ones = 0
        ops = 0
        for i in reversed(range(n)):
            ops += ones
            if boxes[i] == "1":
                ones += 1
            ans[i] += ops
        
        return ans