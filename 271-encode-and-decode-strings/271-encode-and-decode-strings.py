class Codec:
    def __init__(self):
        self.map = {chr(i): f"a{i}" for i in range(256)}
        self.rmap = {f"{i}": chr(i)  for i in range(256)}
            
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        estr = []
        for s in strs:
            for c in s:
                estr.append(self.map[c])
            estr.append('|')
        estr.pop()
        return "".join(estr)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        dstr = []
        for ss in s.split('|'):
            dss = []
            for c in ss.split('a'):
                if c:
                    dss.append(self.rmap[c])
            dstr.append("".join(dss))
        return dstr


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))