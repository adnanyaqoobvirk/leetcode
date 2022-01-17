class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        starts = sorted(start for start, _ in intervals)
        ends = sorted(end for _, end in intervals)
        max_rooms = rooms = sp = ep = 0
        while sp < n and ep < n:
            if starts[sp] < ends[ep]:
                rooms, sp = rooms + 1, sp + 1
            else:
                rooms, ep = rooms - 1, ep + 1
            max_rooms = max(max_rooms, rooms)
        return max_rooms