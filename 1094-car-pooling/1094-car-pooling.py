class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = [0] * 1001
        for pcount, pick, drop in trips:
            events[pick] += pcount
            events[drop] += -pcount
        
        curr_cap = 0
        for i in range(1001):
            curr_cap += events[i]
            if curr_cap > capacity:
                return False
        return True