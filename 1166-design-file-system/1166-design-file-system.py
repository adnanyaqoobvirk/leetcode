class FileSystem:

    def __init__(self):
        self.trie = {}

    def createPath(self, path: str, value: int) -> bool:
        folders = path.split("/")
        t = self.trie
        for i in range(1, len(folders) - 1):
            f = folders[i]
            if not f or f not in t:
                return False
            t = t[f]
        f = folders[-1]
        if f not in t:
            t[f] = {}
        else:
            return False
        t[f]["#"] = value
        return True

    def get(self, path: str) -> int:
        folders = path.split("/")
        t = self.trie
        for i in range(1, len(folders)):
            f = folders[i]
            if not f or f not in t:
                return -1
            t = t[f]
        return t["#"]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)