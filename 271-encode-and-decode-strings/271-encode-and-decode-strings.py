class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return chr(257).join(strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(chr(257))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))