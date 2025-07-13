class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        res = 0
        players.sort()
        trainers.sort(reverse=True)
        for t in trainers:
            while players and players[-1] > t:
                players.pop()
            if players:
                players.pop()
                res += 1
            else:
                break
        return res