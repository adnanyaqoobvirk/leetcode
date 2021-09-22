class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = bcount = 0
        for boxes, units in boxTypes:
            for _ in range(boxes):
                bcount += 1
                ans += units
                if bcount >= truckSize:
                    break
            else:
                continue
            break
        return ans