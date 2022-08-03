class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.heap = []
        self.tokens = {}
    
    def generate(self, tokenId: str, currentTime: int) -> None:
        heappush(self.heap, (currentTime, tokenId))
        self.tokens[tokenId] = 1

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.removeExpired(currentTime)
        if tokenId in self.tokens:
            heappush(self.heap, (currentTime, tokenId))
            self.tokens[tokenId] += 1

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.removeExpired(currentTime)
        return len(self.tokens)
    
    def removeExpired(self, currentTime: int) -> None:
        while self.heap and currentTime - self.heap[0][0] >= self.timeToLive:
            _, token = heappop(self.heap)
            self.tokens[token] -= 1
            if self.tokens[token] == 0:
                del self.tokens[token]
        
                
# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)