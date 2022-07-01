class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        counts = defaultdict(int)
        for boxes, units in boxTypes:
            counts[units] += boxes
        
        ans = 0
        for units in reversed(range(1001)):
            boxes = counts[units]
            ans += min(boxes, truckSize) * units
            truckSize -= boxes
            if truckSize <= 0:
                break
        return ans