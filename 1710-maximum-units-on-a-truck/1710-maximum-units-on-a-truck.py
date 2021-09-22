class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        counts = {}
        for boxes, units in boxTypes:
            counts[units] = counts.get(units, 0) + boxes
        
        ans = 0
        for units in range(1000, 0, -1):
            boxes = counts.get(units, 0)
            if boxes:
                truckSize -= boxes
                if truckSize > 0:
                    ans += boxes * units
                else:
                    ans += (boxes + truckSize) * units
                    break
        return ans