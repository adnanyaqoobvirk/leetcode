class FileSystem:

    def __init__(self):
        self.trie = {}

    def ls(self, path: str) -> List[str]:
        t = self.trie
        for d in path.split("/"):
            if d:
                if d not in t:
                    t[d] = {}
                t = t[d]
        if type(t) == str:
            return [d]
        else:
            return sorted(t.keys())

    def mkdir(self, path: str) -> None:
        t = self.trie
        for d in path.split("/"):
            if d:
                if d not in t:
                    t[d] = {}
                t = t[d]

    def addContentToFile(self, filePath: str, content: str) -> None:
        t, sp = self.trie, filePath.split("/")
        for i in range(len(sp) - 1):
            d = sp[i]
            if d:
                if d not in t:
                    t[d] = {}
                t = t[d]
            
        d = sp[len(sp) - 1]
        if d not in t:
            t[d] = content
        else:
            t[d] += content
            
    def readContentFromFile(self, filePath: str) -> str:
        t = self.trie
        for d in filePath.split("/"):
            if d:
                if d not in t:
                    t[d] = {}
                t = t[d]
        return t


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)