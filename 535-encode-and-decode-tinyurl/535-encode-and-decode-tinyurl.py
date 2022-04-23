from random import sample

class Codec:
    charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    
    def __init__(self):
        self.map = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = "".join(sample(Codec.charset, 6))
        self.map[key] = longUrl
        return f"http://tinyurl.com/{key}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.split('/')[-1]
        return self.map.get(key, None)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))