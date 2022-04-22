class FileSystem:

    def __init__(self):
        self.paths = defaultdict(int)

    def createPath(self, path: str, value: int) -> bool:
        t = self.paths
        spaths = path.split("/")
        for i in range(1, len(spaths) - 1):
            spath = spaths[i]
            if spath not in t:
                return False
            else:
                t = t[spath]
        if spaths[-1] in t:
            return False
        else:
            t[spaths[-1]] = {"#": value}
            return True

    def get(self, path: str) -> int:
        t = self.paths
        spaths = path.split("/")
        for i in range(1, len(spaths)):
            spath = spaths[i]
            if spath not in t:
                return -1
            else:
                t = t[spath]
        return t["#"]
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)