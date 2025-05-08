class Logger:

    def __init__(self):
        self.mmap = defaultdict(lambda: -inf)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.mmap[message] <= timestamp - 10:
            self.mmap[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)