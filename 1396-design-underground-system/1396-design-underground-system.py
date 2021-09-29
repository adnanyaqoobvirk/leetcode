class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.customers[id]
        
        travelStats = self.times.setdefault((startStation, stationName), [0, 0])
        travelStats[0] = (travelStats[0] * travelStats[1] + t - startTime) / (travelStats[1] + 1)
        travelStats[1] += 1
        
        del self.customers[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.times[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)