from sortedcontainers import SortedList

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.q = deque()
        self.dmap = defaultdict(lambda: SortedList(key=lambda x: x[0]))

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if len(self.q) >= self.limit:
            s, d, t = self.q.popleft()
            self.dmap[d].remove((t, s))

        if (timestamp, source) in self.dmap[destination]:
            return False

        self.q.append((source, destination, timestamp))
        self.dmap[destination].add((timestamp, source))
        return True

    def forwardPacket(self) -> List[int]:
        if self.q:
            source, destination, timestamp = self.q.popleft()
            self.dmap[destination].remove((timestamp, source))
            return [source, destination, timestamp]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        l = self.dmap[destination].bisect_left((startTime, ""))
        r = self.dmap[destination].bisect_right((endTime, ""))
        return r - l


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)