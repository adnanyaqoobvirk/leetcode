class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        losers = defaultdict(int)
        for w, l in matches:
            players.add(w)
            players.add(l)
            losers[l] += 1
        
        return [
            list(sorted(players - set(losers.keys()))), 
            list(sorted(k for k, v in losers.items() if v == 1))
        ]