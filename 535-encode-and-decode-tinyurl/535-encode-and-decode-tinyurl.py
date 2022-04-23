from hashlib import blake2b
from base64 import b64encode

class Codec:
    def __init__(self):
        self.map = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        h = blake2b(digest_size=6)
        h.update(longUrl.encode())
        key = str(b64encode(h.digest())).replace('/','')
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