class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        
        ans = 0
        for boxes, units in boxTypes:
            ans += min(boxes, truckSize) * units
            truckSize -= boxes
            if truckSize <= 0:
                break
        return ans