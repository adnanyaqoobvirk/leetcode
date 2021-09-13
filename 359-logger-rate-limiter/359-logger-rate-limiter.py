class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.old_msgs = {}
        self.curr_msgs = {}
        self.min_time = 0
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp >= self.min_time + 10:
            self.old_msgs = self.curr_msgs
            self.curr_msgs = {}
            self.min_time = timestamp
        
        if message in self.curr_msgs or timestamp < self.old_msgs.get(message, timestamp - 10) + 10:
            return False
        
        self.curr_msgs[message] = timestamp
        return True
        
        



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)