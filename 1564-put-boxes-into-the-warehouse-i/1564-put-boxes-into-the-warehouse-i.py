class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        
        n = len(warehouse)
        ans = i = 0
        for box in boxes:
            if warehouse[i] >= box:
                ans += 1
                i += 1
            if i == n:
                break
        return ans