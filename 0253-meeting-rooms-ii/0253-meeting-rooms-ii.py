class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        pq, rooms = [], 0
        for start, end in intervals:
            while pq and pq[0] <= start:
                heappop(pq)
            heappush(pq, end)
            rooms = max(rooms, len(pq))
        return rooms