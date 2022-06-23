class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        
        h = []
        total_duration = 0
        for duration, last_day in courses:
            heappush(h, -duration)
            total_duration += duration
            if total_duration > last_day:
                total_duration += heappop(h)
        return len(h)