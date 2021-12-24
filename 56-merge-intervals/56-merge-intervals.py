class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        ans, curr_start, curr_end = [], intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if curr_start <= start <= curr_end:
                if end > curr_end:
                    curr_end = end
            else:
                ans.append([curr_start, curr_end])
                curr_start, curr_end = start, end
        ans.append([curr_start, curr_end])
        return ans
            