from string import ascii_letters
from random import sample

class Codec:
    
    def __init__(self):
        self.cache = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        while True:
            random_str = "".join(sample(ascii_letters, 6))
            if random_str not in self.cache:
                self.cache[random_str] = longUrl
                return f'http://tinyurl.com/{random_str}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.cache.get(
            shortUrl.strip('/ ').split('/')[-1], 
            None
        )
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))