class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                res += 1
        return res