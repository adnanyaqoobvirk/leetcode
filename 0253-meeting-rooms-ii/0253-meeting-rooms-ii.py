class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []
        for start, end in intervals:
            starts.append(start)
            ends.append(end)
        
        starts.sort()
        ends.sort()
        
        rooms = i = 0
        for start in starts:
            if start >= ends[i]:
                i += 1
                rooms -= 1
            rooms += 1
        return rooms