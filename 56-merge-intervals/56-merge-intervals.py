class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            (_, curr_end), (start, end) = ans[-1], intervals[i]
            if start <= curr_end:
                ans[-1][1] = max(end, curr_end)
            else:
                ans.append([start, end])
        return ans
            