class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        q = deque(range(n))
        res = [None] * n
        for card in sorted(deck):
            res[q.popleft()] = card
            if q:
                q.append(q.popleft())
        return res