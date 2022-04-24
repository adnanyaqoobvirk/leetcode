class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.avgTimes = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkins[id]
        avgTime = self.avgTimes[(startStation, stationName)]
        avgTime[0] += t - startTime
        avgTime[1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.avgTimes[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)