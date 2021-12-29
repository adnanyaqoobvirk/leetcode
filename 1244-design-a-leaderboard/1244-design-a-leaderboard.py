class Leaderboard:

    def __init__(self):
        self.lb = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.lb[playerId] += score

    def top(self, K: int) -> int:
        h = []
        for v in self.lb.values():
            if len(h) < K:
                h.append(v)
                if len(h) == K:
                    heapify(h)
            elif len(h) >= K and h[0] < v:
                heappushpop(h, v)
        return sum(h)

    def reset(self, playerId: int) -> None:
        self.lb[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)