class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []
        for start, end in intervals:
            points.append((start, 'b'))
            points.append((end, 'a'))
        points.sort()
        
        rooms = ans = 0
        for _, status in points:
            if status == 'b':
                rooms += 1
                ans = max(ans, rooms)
            else:
                rooms -= 1
        return ans