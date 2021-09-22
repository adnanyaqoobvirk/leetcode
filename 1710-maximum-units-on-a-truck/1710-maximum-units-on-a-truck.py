class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for boxes, units in boxTypes:
            truckSize -= boxes
            if truckSize > 0:
                ans += boxes * units
            else:
                ans += (boxes + truckSize) * units
                break
        return ans