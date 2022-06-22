class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        
        n = len(slots2)
        
        left = 0
        for start, end in slots1:
            if end - start < duration:
                continue
            
            while left < n:
                cstart, cend = slots2[left]
                if cend - cstart >= duration:
                    if cstart == start:
                        return [start, start + duration]
                    elif cstart < start:
                        if cend > end or (cend <= end and cend - start >= duration):
                            return [start, start + duration]
                    else:
                        if cend < end or (end <= cend and end - cstart >= duration):
                            return [cstart, cstart + duration]
                        else:
                            break
                left += 1
        return []