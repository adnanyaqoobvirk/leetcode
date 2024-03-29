class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(jobs) : return 0
            k = bisect_left(jobs, jobs[i][1], key = lambda j: j[0])
            return max(dfs(i+1), jobs[i][2] + dfs(k))
        jobs = sorted(zip(startTime, endTime, profit))
        return dfs(0)