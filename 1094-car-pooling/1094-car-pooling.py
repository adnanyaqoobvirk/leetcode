class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = defaultdict(list)
        for pcount, pick, drop in trips:
            events[pick].append(pcount)
            events[drop].append(-pcount)
        
        curr_cap = 0
        for i in range(1001):
            for pcount in events[i]:
                curr_cap += pcount
            if curr_cap > capacity:
                return False
        return True