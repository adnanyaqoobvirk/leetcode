class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h, rooms = [], 0
        for start, end in intervals:
            while h and h[0] <= start:
                heappop(h)
            heappush(h, end)
            rooms = max(rooms, len(h))
        return rooms