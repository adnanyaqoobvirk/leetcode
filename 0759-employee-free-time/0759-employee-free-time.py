"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted((x for s in schedule for x in s), key=lambda x: (x.start, x.end))
        ans = []
        end = intervals[0].start
        for i in intervals:
            if i.start > end:
                ans.append(Interval(end, i.start))
            end = max(end, i.end)
        return ans