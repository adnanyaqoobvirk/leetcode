class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for pcount, f, t in trips:
            events.append((f, pcount))
            events.append((t, -pcount))
        events.sort()
        
        curr_cap = 0
        for t, pcount in events:
            curr_cap += pcount
            if curr_cap > capacity:
                return False
        return True