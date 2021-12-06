class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        estr = []
        for s in strs:
            estr.append(f"{len(s):03}")
            estr.append(s)
        return "".join(estr)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        i = 0
        while i < len(s):
            l = int(s[i:i + 3])
            ans.append(s[i + 3:i + 3 + l])
            i += 3 + l
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))