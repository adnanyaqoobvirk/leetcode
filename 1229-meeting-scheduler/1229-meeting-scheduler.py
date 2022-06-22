class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots = [
            slot
            for slot in slots1
            if slot[1] - slot[0] >= duration
        ]
        for slot in slots2:
            if slot[1] - slot[0] >= duration:
                slots.append(slot)
        
        heapify(slots)
        
        while len(slots) > 1:
            start, end = heappop(slots)
            cstart, cend = slots[0]
            
            if end >= cstart + duration:
                return [cstart, cstart + duration]
        return []
            