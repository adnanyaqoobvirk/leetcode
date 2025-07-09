class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        events = sorted(zip(startTime, endTime))
        events.append((eventTime, eventTime))

        btime = 0
        for i in range(k + 1):
            btime += events[i][1] - events[i][0]

        max_ftime = events[k][1] - btime
        for i in range(k + 1, n + 1):
            btime -= events[i - k - 1][1] - events[i - k - 1][0]
            btime += events[i][1] - events[i][0]
            max_ftime = max(max_ftime, events[i][1] - events[i - k - 1][1] - btime)
        return max_ftime